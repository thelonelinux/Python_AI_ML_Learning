# TOPICS LEARNING AND UNDERSTANDING
* Most of these below topics are already present in notes of modules.

## A. AI, ML, DL
Artificial Intelligence (AI) is the broad field of building machines that can perform tasks that usually require human intelligence, such as reasoning, learning, and decision-making.

Machine Learning (ML) is a subset of AI that enables systems to learn patterns from data and improve their performance without being explicitly programmed for every task.

Deep Learning (DL) is a subset of ML that uses artificial neural networks with many layers to solve complex problems like image recognition, speech processing, and natural language understanding.

### In short
- AI = the broad concept of intelligent machines
- ML = teaching machines using data
- DL = using deep neural networks for complex learning tasks
* Check this below image for overall understanding where each of them lies
![alt text](Ai.png)


## B. Deep Learning (ANN, RNN, CNN etc)

Deep Learning is a branch of machine learning that uses artificial neural networks with many layers to learn complex patterns from large amounts of data. It is especially powerful for tasks such as image recognition, speech recognition, language understanding, and prediction.

### Main Types of Deep Learning Models
- ANN (Artificial Neural Network): A basic neural network used for general-purpose prediction and classification tasks.
- CNN (Convolutional Neural Network): Best for image and video data because it can detect patterns like edges, shapes, and textures.
- RNN (Recurrent Neural Network): Designed for sequential data such as text, time series, and speech.
- LSTM/GRU: Advanced forms of RNNs that are better at remembering long-term information.

### In short
- Deep Learning = learning from data using layered neural networks
- ANN = basic neural network
- CNN = best for images
- RNN = best for sequences



## C. Transformers, Gen AI, and LLMs
Transformers are a neural network architecture that became the foundation of modern AI language models. They use a mechanism called attention, which helps the model focus on the most relevant words or parts of input when processing information.

Generative AI (Gen AI) is a type of AI that can create new content such as text, images, code, music, or videos. It learns patterns from large datasets and then generates new outputs based on those patterns.

Large Language Models (LLMs) are powerful AI models trained on huge amounts of text data. They can understand prompts, answer questions, summarize content, translate languages, and generate human-like text.

### Short notes
- Transformers = the architecture behind most modern GenAI models
- Gen AI = AI that generates new content
- LLMs = large models trained on massive text data for language tasks
- Examples = ChatGPT, Gemini, Claude, Llama


## D. Transformers vs RNN
Transformers and RNNs are both used for sequence-based data such as text, speech, and time series, but they work differently.

RNNs process data one step at a time and pass information through hidden states. This makes them useful for sequential tasks, but they often struggle with long-term memory and training speed.

Transformers process the whole input at once using attention mechanisms. This allows them to capture relationships between words or tokens more effectively, especially over long distances in a sequence.

### Short comparison
- RNN: good for sequential data, but slower and weaker for long contexts
- Transformer: better for long-range dependencies, parallel processing, and modern LLMs
- In simple words: RNN works step by step, while Transformer looks at the whole sequence more efficiently


## E. Langchain for Generative AI
LangChain in one sentence 
LangChain is the glue layer between your application and the LLM, 
providing modular, composable components for prompts, models, memory, 
retrieval, chains, and agents — so you build products, not boilerplate. 

LangChain Ecosystem Overview 
Package             : Purpose 
langchain           : Core abstractions: chains, memory, agents, retrievers 
langchain-openai    : OpenAI-specific integrations (ChatOpenAI, OpenAIEmbeddings) 
langchain-community : Community-contributed integrations (Ollama, HuggingFace, FAISS) 
langchain-core      : Base interfaces and LCEL primitives 
langgraph           : Graph-based stateful agent orchestration 
langserve           : Deploy LangChain chains as REST APIs (FastAPI-based) 
langsmith           : Observability: trace, debug, evaluate LLM app runs 

## F. Retriever (RAG)
A retriever is a component in a RAG (Retrieval-Augmented Generation) system that searches for the most relevant information from a knowledge base before the LLM generates an answer.

In simple words, the retriever helps the model look up useful documents or chunks of information instead of relying only on its training memory.

### Why retriever is used
- To give the model fresh and domain-specific information
- To reduce hallucinations
- To make answers more accurate and grounded in real data

### Good example
Suppose a user asks:
> "What is the refund policy for this company?"

If the system has a knowledge base containing company documents, the retriever searches the documents and finds the most relevant section about refunds. That retrieved text is then passed to the LLM, which uses it to answer the question.

### Simple flow
1. User asks a question
2. Retriever searches the document store
3. Most relevant documents are fetched
4. LLM reads those documents and generates the answer

### In short
- Retriever = search engine for the LLM
- It finds relevant context from documents
- Then the LLM uses that context to answer better


## G. AI Agents

An AI agent is a system that can understand a goal, take actions, and use tools or external resources to complete a task step by step.

Unlike a simple chatbot that only responds to a prompt, an AI agent can plan, reason, and act. It may use tools such as web search, calculators, databases, or APIs to solve a problem.

### Simple example
Suppose you ask an AI agent:
> "Book me a flight to Delhi for next Friday and compare prices."

The agent may:
1. Search travel websites
2. Compare available flights
3. Select the best option
4. Return the result or even complete the booking

### In short
- AI agent = an AI system that can act to achieve a goal
- It uses tools and reasoning
- It is more than just answering questions

