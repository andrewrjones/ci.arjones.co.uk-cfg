dzil_arjones_bundle = {}

####### SCHEDULERS

# Configure the Schedulers, which decide how to react to incoming changes.  In this

from buildbot.schedulers.basic import SingleBranchScheduler
from buildbot.changes import filter

dzil_arjones_bundle['schedulers'] = []
dzil_arjones_bundle['schedulers'].append(SingleBranchScheduler(
                            name="Dist::Zilla::PluginBundle::ARJONES-commit",
                            change_filter=filter.ChangeFilter(project='Dist::Zilla::PluginBundle::ARJONES'),
                            treeStableTimer=None,
                            builderNames=["Dist::Zilla::PluginBundle::ARJONES"]))

####### BUILDERS

# The 'builders' list defines the Builders, which tell Buildbot how to perform a build:
# what steps, and which slaves can execute them.  Note that any particular build will
# only take place on one slave.

from buildbot.process.factory import BuildFactory
from buildbot.steps.source import Git
from buildbot.steps.shell import ShellCommand
from buildbot.config import BuilderConfig

factory_dzil = BuildFactory()
# check out the source
factory_dzil.addStep(Git(repourl='git://github.com/andrewrjones/perl5-Dist-Zilla-PluginBundle-ARJONES.git', mode='copy'))
# run the tests
#factory_dzil.addStep(ShellCommand(command=["source", "../../../perl5/etc/bashrc"]))
factory_dzil.addStep(ShellCommand(command="dzil authordeps | cpanm"))
factory_dzil.addStep(ShellCommand(command="dzil listdeps | cpanm"))
factory_dzil.addStep(ShellCommand(command=["dzil", "smoke"]))
#factory_dzil.addStep(ShellCommand(command=["prove", "-l", "t"]))

dzil_arjones_bundle['builders'] = []
dzil_arjones_bundle['builders'].append(
    BuilderConfig(name="Dist::Zilla::PluginBundle::ARJONES",
      slavenames=["l1"],
      factory=factory_dzil))