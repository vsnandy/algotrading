from typing import Dict
from ms_graph.session import GraphSession

class Users():

    def __init__(self, session: object) -> None:

        # Set the session.
        self.graph_session: GraphSession = session

        # Set the endpoint.
        self.endpiont = 'users'

    def list_users(self) -> Dict:

        content = self.graph_session.make_request(
                method='get',
                endpoint=self.endpoint
                )

        return content
