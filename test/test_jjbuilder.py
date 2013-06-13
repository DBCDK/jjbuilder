from jjbuilder import generate_job
import pytest


def assertJob(data, result_file):
  lines = file(result_file).readlines()
  whole_file = reduce(str.__add__, lines)
  job = generate_job(data)
  assert job == whole_file

def testGenerateEmptyJob():
  assertJob({}, 'test/jobs/empty.xml')

def testGenerateDescribedJob():
  assertJob({'description': 'Some description of the job.'}, 'test/jobs/description.xml')
  assertJob({'description': '<h2>Some description containing a tag</h2> of the job & some "HTML entities" which isn\'t always escaped.'}, 'test/jobs/description_htmlentities.xml')
