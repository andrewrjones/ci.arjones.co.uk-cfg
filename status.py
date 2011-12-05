####### STATUS TARGETS

# 'status' is a list of Status Targets. The results of each build will be
# pushed to these targets. buildbot/status/*.py has a variety to choose from,
# including web pages, email senders, and IRC bots.

status = []

from buildbot.status import html
from buildbot.status.web import authz
authz_cfg=authz.Authz(
    # change any of these to True to enable; see the manual for more
    # options
    gracefulShutdown = False,
    forceBuild = False, # use this to test your slave once it is set up
    forceAllBuilds = False,
    pingBuilder = False,
    stopBuild = False,
    stopAllBuilds = False,
    cancelPendingBuild = False,
)
status.append(html.WebStatus(http_port=8010, authz=authz_cfg, change_hook_dialects={ 'github' : True }))

from buildbot.status import mail
mail_status = mail.MailNotifier(fromaddr="buildbot@arjones.co.uk",
                      extraRecipients=["andrewjones86@gmail.com"],
                      sendToInterestedUsers=False)
status.append(mail_status)