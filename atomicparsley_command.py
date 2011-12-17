ap = {}

####### SCHEDULERS

# Configure the Schedulers, which decide how to react to incoming changes.  In this

from buildbot.schedulers.basic import SingleBranchScheduler
from buildbot.changes import filter

ap['schedulers'] = []
ap['schedulers'].append(SingleBranchScheduler(
                            name="AtomicParsley::Command-commit",
                            change_filter=filter.ChangeFilter(project='AtomicParsley::Command'),
                            treeStableTimer=60,
                            builderNames=["AtomicParsley::Command"]))

####### BUILDERS

# The 'builders' list defines the Builders, which tell Buildbot how to perform a build:
# what steps, and which slaves can execute them.  Note that any particular build will
# only take place on one slave.

from buildbot.process.factory import BuildFactory
from buildbot.steps.source import Git
from buildbot.steps.shell import ShellCommand
from buildbot.config import BuilderConfig

from modules.dzil_steps.dzil import DzilSmoke

factory_ap = BuildFactory()
# check out the source
factory_ap.addStep(Git(repourl='git://github.com/andrewrjones/perl5-AtomicParsley-Command.git', mode='copy'))
# run the tests (note that this will require that 'trial' is installed)
#factory_ap.addStep(ShellCommand(command=["source", "../../../perl5/etc/bashrc"]))
factory_ap.addStep(ShellCommand(command="dzil authordeps | cpanm"))
factory_ap.addStep(ShellCommand(command="dzil listdeps | cpanm"))
factory_ap.addStep(DzilSmoke())
#factory_ap.addStep(ShellCommand(command=["prove", "-l", "t"]))

ap['builders'] = []
ap['builders'].append(
    BuilderConfig(name="AtomicParsley::Command",
      slavenames=["l1"],
      factory=factory_ap))