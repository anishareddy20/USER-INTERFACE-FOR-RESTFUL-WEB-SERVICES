# USER-INTERFACE-FOR-RESTFUL-WEB-SERVICES
The web application run on url: http://ec2-18-218-84-2.us-east-2.compute.amazonaws.com:8000

It implements an UI for Restful web services. It is a dynamic approach which is implemented using AJAX request and java script. It is a web application where the user should give a date in web browser and click submit button and it takes forecast data given by restful web service and plots graph for the TMAX and TMIN values obtained. The forecast data gives TMAX and TMIN values for 7 days from given date.

Additionally, we also plot the graph for the data obtained from a third-party server. Here the third-party data used is forecast weather information for 5 days from given date by accuweather. The graph is plotted using data from API.

To create this web application the technologies used are HTML,AJAX,CSS,JAVASCRIPT,JQUERY,GOOGLE CHARTS.

The web application is hosted on AWS ubuntu instance on port 8000

To keep this web application running we need to host it on gunicorn ngix.

This application runs best on Google chrome.

STEPS: •	Launch AWS ubuntu instance and adding port 8000 in security groups. •	Install gunicorn nginx •	Create a folder and add the html file in to folder. •	Keep running the nginx and check the EC2 dns name in browser with port 8000

References to install ngnix: http://timmyreilly.azurewebsites.net/running-flask-on-ubuntu-vm/?fbclid=IwAR0G94SCqolQd5-psl-w5SugWiYDFkb79tqlDeHTYhdXZPlcPvQ4-NEAQQE
