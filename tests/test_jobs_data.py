"""Data integrity tests use invented fixtures; no fixtures enter the public dataset."""
import copy
import unittest
from html.parser import HTMLParser
from tools.validate_jobs import validate_dataset, load_json, ROOT
from tools.build_job_sources import validate_sources, render


def sample():
    job = {
        'id':'fixture-job-1','source_id':'ge-healthcare','source_job_id':'fixture-1',
        'employer':{'id':'fixture-employer','name':'Example employer','type':'oem_manufacturer'},
        'title':'BMET II','role_type':'bmet','level':'intermediate',
        'location':{'city':'Example','state':'PA','country':'US'},'workplace_type':'onsite',
        'url':'https://example.com/jobs/1','posted_at':None,
        'first_seen':'2026-09-28T12:00:00Z','last_seen':'2026-09-28T12:00:00Z',
        'status':'active','salary':None,
    }
    return {'schema_version':1,'updated_at':job['last_seen'],'coverage_status':'collecting',
            'jobs':[job],'observations':[{'job_id':job['id'],'observed_at':job['last_seen'],'snapshot':copy.deepcopy(job)}]}


class JobsDataTests(unittest.TestCase):
    def setUp(self):
        self.sources = load_json(ROOT/'data/job-sources.json')

    def test_committed_data_and_sources(self):
        self.assertEqual(validate_dataset(load_json(ROOT/'data/jobs.json'),self.sources),[])
        validate_sources(self.sources)

    def test_page_has_unique_anchors_and_one_main_heading(self):
        class Parser(HTMLParser):
            def __init__(self):
                super().__init__()
                self.ids=[]
                self.h1s=0
            def handle_starttag(self,tag,attrs):
                attrs=dict(attrs)
                if 'id' in attrs:
                    self.ids.append(attrs['id'])
                self.h1s += tag=='h1'
        page=Parser()
        page.feed((ROOT/'biomed-jobs.html').read_text(encoding='utf-8'))
        self.assertEqual(page.h1s,1)
        self.assertEqual(len(page.ids),len(set(page.ids)))
        self.assertTrue({'page-heading','quick-searches','linkedin-searches','job-titles','employers'} <= set(page.ids))

    def test_observed_job_and_closure_retain_history(self):
        before = sample()
        after = copy.deepcopy(before)
        after['updated_at'] = '2026-09-29T12:00:00Z'
        after['jobs'][0].update(status='closed', last_seen=after['updated_at'])
        after['observations'].append({'job_id':'fixture-job-1','observed_at':after['updated_at'],'snapshot':copy.deepcopy(after['jobs'][0])})
        self.assertEqual(validate_dataset(after,self.sources,previous=before),[])

    def test_history_tampering_and_deletion_fail(self):
        before=sample()
        changed=copy.deepcopy(before)
        changed['observations'][0]['snapshot']['title']='Rewritten past'
        self.assertTrue(validate_dataset(changed,self.sources,previous=before))
        changed=copy.deepcopy(before)
        changed['jobs']=[]
        changed['observations']=[]
        self.assertTrue(any('retain job' in e for e in validate_dataset(changed,self.sources,previous=before)))

    def test_bad_dates_source_urls_and_salary_fail(self):
        for field,value in [('source_id','missing-source'),('url','javascript:alert(1)'),('last_seen','2026-02-30T12:00:00Z'),('salary',{'min':90,'max':20,'currency':'USD','period':'hour'}),('role_type','invented-role')]:
            with self.subTest(field=field):
                data=sample()
                data['jobs'][0][field]=value
                self.assertTrue(validate_dataset(data,self.sources))

    def test_duplicate_urls_cannot_inflate_counts(self):
        data=sample()
        duplicate=copy.deepcopy(data['jobs'][0])
        duplicate.update(id='fixture-job-2',source_job_id='fixture-2',url='https://EXAMPLE.com/jobs/1/#section')
        data['jobs'].append(duplicate)
        self.assertTrue(any('duplicate job URL' in e for e in validate_dataset(data,self.sources)))

    def test_not_started_is_not_zero_vacancies(self):
        data=sample()
        data['coverage_status']='not_started'
        self.assertTrue(any('not_started' in e for e in validate_dataset(data,self.sources)))

    def test_sources_escape_text_and_reject_unsafe_urls(self):
        data=copy.deepcopy(self.sources)
        data['sources'][0]['name']='<script>alert(1)</script>'
        output=render(validate_sources(data))
        self.assertNotIn('<script>',output)
        self.assertIn('&lt;script&gt;',output)
        data['sources'][0]['url']='javascript:alert(1)'
        with self.assertRaises(ValueError):
            validate_sources(data)

    def test_source_ids_must_be_unique(self):
        data=copy.deepcopy(self.sources)
        data['sources'].append(data['sources'][0])
        with self.assertRaises(ValueError):
            validate_sources(data)


if __name__ == '__main__':
    unittest.main()
