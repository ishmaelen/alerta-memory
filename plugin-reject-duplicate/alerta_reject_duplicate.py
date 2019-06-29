import logging

from alerta.exceptions import RejectException
from alerta.plugins import PluginBase

LOG = logging.getLogger('alerta.plugins')

class RejectDuplicate(PluginBase):

    def pre_receive(self, alert, **kwargs):

        ''' 
        Do nothing witin incoming alerts.  We want to process them all because there is not
        enough information in just the submitted alert to make an accept/reject decision
        '''

        return alert

    def post_receive(self, alert):

        ignore_env = ['env1', 'env2', 'env3']
        ignore_sev = ['cleared', 'normal', 'ok'] 

        '''
        ONLY FOR SPECIFIED ENVIRONMENTS....
        We want to delete any alert that is "normal" (meaning not an issue) and has been around for
        at least three duplication iterations.  We also want to delete any incoming alerts that come
        in as "normal" and the previous severity is "indeterminate".  That would be an OK check coming
        in from a previously deleted alert.
        '''

        if alert.environment in ignore_env and alert.severity in ignore_sev and alert.duplicate_count > 2:
            alert.delete()
        
        if alert.environment in ignore_env and alert.severity in ignore_sev and alert.previous_severity == "indeterminate":
            alert.delete()

        return 

    def status_change(self, alert, status, text):

        return
