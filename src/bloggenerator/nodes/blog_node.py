from bloggenerator.states.blog_state import BlogState


class BlogNode:
    """A class representing a blog node."""

    def __init__(self, llm):
        self.llm = llm

    def title_creation(self,state:BlogState):
        """
        Generate a title for the blog based on the topic.
        """


        if 'topic' in state and state['topic']:
            prompt = """ 
                        Your are expert bog content write .Use Mark down formatting. Genrate a blog title for the {topic}. this title should be creative and SEO friendly
                     """

            system_message= prompt.format(topic=state['topic'])
            response = self.llm.invoke(system_message)
        return {'blog':{'title':response.content}}

    def content_genration(self,state:BlogState):
        if 'topic' in state and state['topic']:
            system_prompt ="""You are axpert blog writer. Use Markdown formatting.
            Generate a detailed blog content with detailed break down for the {topic}"""

            system_message= system_prompt.format(topic=state['topic'])
            response = self.llm.invoke(system_message)
            return {'blog' : {'title': state['blog']['title'], 'content': response.content}}


