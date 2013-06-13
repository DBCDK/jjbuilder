import jenkins
from StringIO import StringIO
from simpletal import simpleTAL, simpleTALES


def generate_job(data):
  context = simpleTALES.Context()

  for key in data.keys():
    context.addGlobal(key, data[key])

  template_file = open('templates/config.xml', 'rt')
  template = simpleTAL.compileXMLTemplate(template_file)
  template_file.close()
  output = StringIO()
  template.expand(context, output, outputEncoding='utf-8')
  return output.getvalue()
