# bankBot-Chatterbot
## _Welcome to ChatBot of simple usage of chatterbot_
## _Members:_
| Name | No Matric |
| ------ | ------ |
| MUHAMMAD FAHMI BIN KAMARUDDIN | B031910259|
| FAIRUZ HAZMAN BIN MAHAD   | B031910270|
| MOHAMAD SAMUDRA NUSANTARA | B031910454|
| ALI ABDULLAH ALI ABDULLAH ALHUSAM | B031910502|
| MOHAMMED SADEQ NOMAN  |  B031910498 |

## ChatBot with interactive UI using simple web socket server
- Chatbot_train.py file trains the data available in the data folder. Once it is trained , the result will be stored as - db.sqlite.
- Chatbot.py uses this db.sqlite to generate responses for user queries.
- server.py sends back message to the client.
- Still Working in Progress with adding text-to-speech feature.

## How to run
Run python server.py.
Above step will open the server. Now right click the index.html page and open with brower. You will be able to see the chat window where you can start the conversation.

## DEFINING THE PROJECT
1.1 Project Summary
	During the old times, people have been making inquiries related to banking by going to the bank and directly asking the staff there. This method was used for a long time when online inquiry was not a thing back then. This has totally been deemed a hassle that people have to make their way to the bank, take numbers for their turn, and ask the bank staff directly for banking-related matters. It is when online inquiries are created where people can communicate with the staff just by asking the questions online and answers are provided by the staff themselves. Although this has made lives easier, it is still not considered the best way to do banking-related matters as it needs a physical staff to actually manage this manually. As time goes on, technology has been improved further to the point where no more staff are needed to manage any banking-related inquiries because chatbots are finally introduced. Chatbot is basically a “virtual staff” that helps a company intelligently answer any questions given by every user on the internet accurately on its own. In this case, a banking chatbot was created to increase the quality of life of users who intend to ask any questions related to banking.

>Customer: Maybank2u.

>Project name: BANKING SERVICE CHATBOT.

Team Members:
- Muhammad Fahmi bin Kamaruddin
- Fairuz Hazman bin Mahad
- Mohamad Samudra Nusantara
- Ali Abdullah Al Husam
- MOHAMMED SADEQ NOMAN
	
2.1 Objectives
To train a model with banking-related questions as training data.
To create a chatbot that answers any banking-related questions.
To create a website and implement the chatbot in it.

## Project Management Life-Cycle


2.2 Risk Identification Chart (Quality, Cost, Time)
|Control Element |What is likely to go wrong?|How and when will I know?|What will I do about it?|
| ------ | ------ |------ |------ |
|  Quality|Prediction of words that aren't correct | When we do testing| We will use more data to train the system. |
|Cost| Internet use is quite high.|When we train the system continuously.|Discuss the use of the internet with the sponsor.|
|Time|Time to scrap the data|When we train the data.|Use a different method instead of scraping.|
