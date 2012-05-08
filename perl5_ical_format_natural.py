perl5_ical_format_natural = {}

####### SCHEDULERS

# Configure the Schedulers, which decide how to react to incoming changes.  In this

from buildbot.schedulers.basic import SingleBranchScheduler
from buildbot.changes import filter

perl5_ical_format_natural['schedulers'] = []
perl5_ical_format_natural['schedulers'].append(SingleBranchScheduler(
                            name="perl5-ICal-Format-Natural-commit",
                            change_filter=filter.ChangeFilter(project='perl5-ICal-Format-Natural'),
                            treeStableTimer=60,
                            builderNames=["perl5-ICal-Format-Natural"]))

####### BUILDERS

# The 'builders' list defines the Builders, which tell Buildbot how to perform a build:
# what steps, and which slaves can execute them.  Note that any particular build will
# only take place on one slave.

from buildbot.process.factory import BuildFactory
from buildbot.steps.source import Git
from buildbot.steps.shell import ShellCommand
from buildbot.config import BuilderConfig

from modules.dzil_steps.dzil import DzilAuthorDependencies, DzilDependencies, DzilSmokeVerbose

factory_perl5_ical_format_natural = BuildFactory()
# check out the source
factory_perl5_ical_format_natural.addStep(Git(repourl='git://github.com/andrewrjones/perl5-ICal-Format-Natural.git', mode='copy'))
# update deps
factory_perl5_ical_format_natural.addStep(DzilAuthorDependencies())
factory_perl5_ical_format_natural.addStep(DzilDependencies())
# run the tests
factory_perl5_ical_format_natural.addStep(DzilSmokeVerbose())

factory_perl5_ical_format_natural['builders'] = []
factory_perl5_ical_format_natural['builders'].append(
    BuilderConfig(name="perl5-ICal-Format-Natural",
      slavenames=["mac"],
      factory=factory_perl5_ical_format_natural))