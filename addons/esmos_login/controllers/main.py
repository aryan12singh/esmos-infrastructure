from odoo import http
from odoo.addons.auth_signup.controllers.main import AuthSignupHome
from werkzeug.utils import redirect

JIRA_URL = 'https://smu-team-ymiz3qlk.atlassian.net/servicedesk/customer/portal/1/group/1/create/3'


class EsmosSignupRedirect(AuthSignupHome):
    """
    Override /web/signup so that anyone who navigates there directly
    (e.g. by typing the URL) is redirected to the Jira Service Desk
    instead of seeing a registration form.
    """

    @http.route('/web/signup', type='http', auth='none', sitemap=False)
    def web_auth_signup(self, *args, **kw):
        return redirect(JIRA_URL, code=302)
