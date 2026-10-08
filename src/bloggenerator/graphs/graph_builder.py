from langgraph.graph import StateGraph, START, END
from bloggenerator.states.blog_state import BlogState
from src.bloggenerator.nodes.blog_node import BlogNode
from src.bloggenerator.llms.openapillm import OpenAILLM


class GraphBuilder:
    def __init__(self,llm):
        self.llm = llm
        self.graph = StateGraph(BlogState)

    def build_topic_graphic(self):
        """
        Build a graph for the topic generation process.
        
        """

        ## Nodes
        self.blog_node_obj= BlogNode(self.llm)

        self.graph.add_node("title_creation", self.blog_node_obj.title_creation)
        self.graph.add_node("content_generation",self.blog_node_obj.content_generation)

        ## Edges
        self.graph.add_edge(START, "title_creation")
        self.graph.add_edge("title_creation", "content_generation")
        self.graph.add_edge("content_generation", END)
        return self.graph

    def build_language_graph(self):
        """
        Build a graph for blog genration with topic and laguage 
        """
        self.blog_node_obj= BlogNode(self.llm)
        ### Nodes
        self.graph.add_node("title_creation", self.blog_node_obj.title_creation)
        self.graph.add_node("content_generation",self.blog_node_obj.content_generation)
        self.graph.add_node("translation", self.blog_node_obj.translation)


        ## Add edges
        self.graph.add_edge(START, "title_creation")
        self.graph.add_edge("title_creation", "content_generation")
        self.graph.add_edge("content_generation", "translation")
        self.graph.add_edge("translation", END)
        return self.graph

    def setup_graph(self,usecase):
        if usecase == "topic" :
            self.build_topic_graphic()
        if usecase == 'language':
            self.build_language_graph()
             
        return self.graph.compile()


### Below code is for the langsmith lang graph studio

llm=OpenAILLM().get_llm()

## get graph
graph_builder=GraphBuilder(llm=llm)
graph=graph_builder.build_language_graph().compile()
  