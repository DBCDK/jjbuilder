from jjbuilder import generate_job
import pytest


def assertJob(data, result_file):
  lines = file('test/jobs/' + result_file).readlines()
  whole_file = reduce(str.__add__, lines)
  job = generate_job(data)
  assert job == whole_file

def testGenerateEmptyJob():
  assertJob({}, 'empty.xml')

def testGenerateDescribedJob():
  assertJob({'description': 'Some description of the job.'}, 'description.xml')
  assertJob({'description': '<h2>Some description containing a tag</h2> of the job & some "HTML entities" which isn\'t always escaped.'}, 'description_htmlentities.xml')

def testAssignedNode():
  assertJob({'assignedNode': 'guesstimate-head'}, 'assignednode.xml')
