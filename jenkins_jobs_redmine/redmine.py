import xml.etree.ElementTree as XML

def redmine_properties(parser, xml_parent, data):
    """yaml: redmine

    Example::

      properties:
        - redmine:
            redmine-website-name: mysite
						project-name: myproject
    """
    if data is None:
        data = dict()

    notifier = XML.SubElement(
        xml_parent, 'hudson.plugins.redmine.RedmineProjectProperty')
    notifier.set('plugin', 'redmine@0.15')

    for opt, attr in (('redmine-website-name', 'redmineWebsiteName'),
                      ('project-name', 'projectName')):
        (XML.SubElement(notifier, attr)
         .text) = data.get(opt)
