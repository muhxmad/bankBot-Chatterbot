# bankBot-Chatterbot
## _Welcome to ChatBot of simple usage of chatterbot_


## ChatBot with interactive UI using simple web socket server
- Chatbot_train.py file trains the data available in the data folder. Once it is trained , the result will be stored as - db.sqlite.
- Chatbot.py uses this db.sqlite to generate responses for user queries.
- server.py sends back message to the client.
- Still Working in Progress with adding text-to-speech feature.

## How to run
Run python server.py.
Above step will open the server. Now right click the index.html page and open with brower. You will be able to see the chat window where you can start the conversation.

## DEFINING THE PROJECT

During the old times, people have been making inquiries related to banking by going to the bank and directly asking the staff there. This method was used for a long time when online inquiry was not a thing back then. This has totally been deemed a hassle that people have to make their way to the bank, take numbers for their turn, and ask the bank staff directly for banking-related matters. It is when online inquiries are created where people can communicate with the staff just by asking the questions online and answers are provided by the staff themselves. Although this has made lives easier, it is still not considered the best way to do banking-related matters as it needs a physical staff to actually manage this manually. As time goes on, technology has been improved further to the point where no more staff are needed to manage any banking-related inquiries because chatbots are finally introduced. Chatbot is basically a “virtual staff” that helps a company intelligently answer any questions given by every user on the internet accurately on its own. In this case, a banking chatbot was created to increase the quality of life of users who intend to ask any questions related to banking.

Customer: Maybank2u.</br>

Project name: BANKING SERVICE CHATBOT.</br>

Team Members:
| Name | No Matric |Role|
| ------ | ------ |------ |
| MUHAMMAD FAHMI BIN KAMARUDDIN | B031910259|Project Manager|
| FAIRUZ HAZMAN BIN MAHAD   | B031910270|Finance Manager|
| MOHAMAD SAMUDRA NUSANTARA | B031910454|Financial Analyst|
| ALI ABDULLAH ALI ABDULLAH ALHUSAM | B031910502|Risk Manager|
| MOHAMMED SADEQ NOMAN  |  B031910498 |Quality Manager|
	
2.1 Objectives</br>
To train a model with banking-related questions as training data.
To create a chatbot that answers any banking-related questions.
To create a website and implement the chatbot in it.

## Project Management Life-Cycle


2.2 Risk Identification Chart (Quality, Cost, Time)</br>
|Control Element |What is likely to go wrong?|How and when will I know?|What will I do about it?|
| ------ | ------ |------ |------ |
|  Quality|Prediction of words that aren't correct | When we do testing| We will use more data to train the system. |
|Cost| Internet use is quite high.|When we train the system continuously.|Discuss the use of the internet with the sponsor.|
|Time|Time to scrap the data|When we train the data.|Use a different method instead of scraping.|

## Project Code Explanation
Executing the project</br>
<div align="center">
Project Webpage Design</br>
<img src="/video/homepage.png" alt="htmlCode"/>
</div>
</br>
<div align="center">
Code for training dataset</br>
<img src="/video/chatbotTrain.png" alt="trainCode"/>
<p>This code is for training the model. It takes data from the training datasets of compiled questions in YML files located in the “data” folder. Once it is trained, the results are stored as db.sqlite.</p>
</div>
</br>
<div align="center">
Code for generating responses to queries (chatbot.py)</br>
<img src="/video/chatbot1.png" alt="coding1"/>
<img src="/video/chatbot2.png" alt="coding2"/>
<img src="/video/chatbot3.png" alt="coding3"/>
<img src="/video/chatbot4.png" alt="coding4"/>
<img src="/video/chatbot5.png" alt="coding5"/>
<img src="/video/chatbot6.png" alt="coding6"/>
<img src="/video/chatbot7.png" alt="coding7"/>
</br>
<p>This code is for testing the chatbot with the testing dataset that is saved in an excel file called “BankFAQs.csv”. Then, it uses the db.sqlite from the training process to generate the responses for user queries.</p>
</div>
</br>
<div align="center">
 Code for connecting chatbot to server (server.py)</br>
<img src="/video/server.png" alt="server"/>
</div></br>

## Project Video Presentation
<div align="center">
  <a href="https://youtu.be/mGz3YAYn5CQ"><img src="https://img.youtube.com/vi/mGz3YAYn5CQ/0.jpg" alt="IMAGE ALT TEXT"></a>
</div>
