from bloggenerator.states.blog_state import BlogState
from langchain_core.messages import HumanMessage
from src.bloggenerator.states.blog_state import Blog


class BlogNode:
    """
    A class to represent he blog node
    """

    def __init__(self,llm):
        self.llm=llm

    
    def title_creation(self,state:BlogState):
        """
        create the title for the blog
        """

        if "topic" in state and state["topic"]:
            prompt="""
                   You are an expert blog content writer. Use Markdown formatting. Generate
                   a blog title for the {topic}. This title should be creative and SEO friendly

                   """
            
            sytem_message=prompt.format(topic=state["topic"])
            print(sytem_message)
            response=self.llm.invoke(sytem_message)
            print(response)
            return {"blog":{"title":response.content}}
        
    def content_generation(self,state:BlogState):
        if "topic" in state and state["topic"]:
            system_prompt = """You are expert blog writer. Use Markdown formatting.
            Generate a detailed blog content with detailed breakdown for the {topic}"""
            system_message = system_prompt.format(topic=state["topic"])
            response = self.llm.invoke(system_message)
            return {"blog": {"title": state['blog']['title'], "content": response.content}}
        
    def translation(self,state:BlogState):
        """
        Translate the content to the specified language.
        """
        translation_prompt = """
        Translate the blog title and content into {current_language}.
        - Keep both the title and content entirely in {current_language}.
        - Maintain the original tone, style, and Markdown formatting.
        - Adapt cultural references and idioms naturally.
        - Return only the translated title and content.

        BLOG TITLE:
        {blog_title}

        BLOG CONTENT:
        {blog_content}
        """
        blog = state["blog"]
        translated_blog = self.llm.with_structured_output(Blog).invoke(
            [
                HumanMessage(
                    translation_prompt.format(
                        current_language=state["current_language"],
                        blog_title=blog["title"],
                        blog_content=blog["content"],
                    )
                )
            ]
        )
        return {"blog": translated_blog}
