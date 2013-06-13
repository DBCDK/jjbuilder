from jjbuilder import generate_job
import pytest


def testGenerateJob():
  lines = file('test/jobs/empty.xml').readlines()
  whole_file = reduce(str.__add__, lines)
  job = generate_job({})
  assert job == whole_file
