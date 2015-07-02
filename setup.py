from setuptools import setup

setup(
    name='jenkins-jobs-redmine',
    version='0.0.1',
    description='Jenkins Job Builder Redmine Plugin',
    url='https://github.com/jovandeginste/jenkins-jobs-redmine',
    author='Jo Vandeginste',
    author_email='jo.vandeginste@gmail.com',
    license='MIT license',
    install_requires=[],
    entry_points={
        'jenkins_jobs.properties': [
            'redmine = jenkins_jobs_redmine.redmine:redmine_properties'],
        'jenkins_jobs.publishers': [
            'redmine = jenkins_jobs_redmine.redmine:redmine_publisher']},
    packages=['jenkins_jobs_redmine'],
    classifiers=[
        'Environment :: Console',
        'Intended Audience :: Developers',
        'Intended Audience :: Information Technology',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3'])
