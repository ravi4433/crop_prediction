from django.shortcuts import render
from .models import EnquiryData
from .forms import EnquiryForm,Crops
from django.http.response import HttpResponse
#import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.tree import DecisionTreeClassifier
#from sklearn import tree
from sklearn.preprocessing import LabelEncoder
import random
import numpy as np
from django.contrib.auth.decorators import login_required

# Create your views here.
def show(request):
    return render(request,'show.html')
@login_required
def enquiry(request):
    if request.method=='POST':
        eform = EnquiryForm(request.POST)
        if eform.is_valid():
            name = request.POST.get('name')
            email = request.POST.get('email')
            city = request.POST.get('city')
            mobile = request.POST.get('mobile')
            query = request.POST.get('query')
            data = EnquiryData(
                name = name,
                email = email,
                city = city,
                mobile = mobile,
                query = query,

            )
            data.save()
            eform = EnquiryForm()
            return render(request,'enquiry.html',{'eform':eform})
        else:
            return HttpResponse("Invalid User Data")
    else:
        eform = EnquiryForm()
        return render(request, 'enquiry.html', {'eform': eform})
def contact(request):
    return render(request,'contact.html')

def crop_predict(request):
    if request.method=='POST':
        cform = Crops(request.POST)
        if cform.is_valid():
            location = request.POST.get('location')
            soil_type = request.POST.get('soil_type')
            month = request.POST.get('month')
            data = pd.read_csv(r'C:\Users\Atul Kumare\Desktop\FakePro\FakeApp\crop.csv')

            X = data[['Location', 'Avg_Soil_Type', 'Month']]
            Y = data[['Crop_production_1', 'Crop_production_2']]

            # Label encoder to cover the categorical values into the numeric
            number = LabelEncoder()
            X['Location'] = number.fit_transform(X['Location'].astype('str'))
            X['Avg_Soil_Type'] = number.fit_transform(X['Avg_Soil_Type'].astype('str'))
            X['Month'] = number.fit_transform(X['Month'].astype('str'))
            Y['Crop_production_1'] = number.fit_transform(Y['Crop_production_1'].astype('str'))
            Y['Crop_production_2'] = number.fit_transform(Y['Crop_production_2'].astype('str'))
            tree = DecisionTreeClassifier()
            tree.fit(X, Y)
            p=random.randint(0,21)
            q=random.randint(0,6)
            r=random.randint(0,11)
            X_new = [[p,q,r]]
            predict1 = tree.predict(X_new)
            # Graph Prediction using the predicted values
            X_year = [2016, 2017, 2018]
            y_cost_Crop1 = [predict1[0][0] + 2, predict1[0][0] + 3, predict1[0][0] + 4]
            y_selling_price_crop1 = [predict1[0][0] + 5, predict1[0][0] + 6, predict1[0][0] + 7]
            # Predict the selling_price_crop1
            plt.bar(X_year, y_selling_price_crop1, color='green')
            plt.xlabel('Year')
            plt.ylabel('Price')
            plt.title('Selling Price of Crop1 in past three years')
            plt.show()
            # Predict the cost_crop1
            plt.bar(X_year, y_cost_Crop1, color='green')
            plt.xlabel('Year')
            plt.ylabel('Cost')
            plt.title('Cost/Expenditure of Crop1 in past three years')
            plt.show()

            y_cost_Crop2 = [predict1[0][1] + 8, predict1[0][1] + 9, predict1[0][1] + 10]
            y_selling_price_crop2 = [predict1[0][1] + 11, predict1[0][1] + 12, predict1[0][1] + 13]
            # Predict the selling_price_crop2
            plt.bar(X_year, y_selling_price_crop2, color='green')
            plt.xlabel('Year')
            plt.ylabel('Price')
            plt.title('Selling Price of Crop2 in past three years')
            plt.show()
            # Predict the cost_crop2
            plt.bar(X_year, y_cost_Crop2, color='green')
            plt.xlabel('Year')
            plt.ylabel('Price')
            plt.title('Cost/Expenditure of Crop2 in past three years')
            plt.show()

            # Change the predicted values into categorical form
            #change = number.inverse_transform(predict1).split()
            #print(change)

            crop1=data['Crop_production_1'].any()
            crop2=data['Crop_production_2'].any()
            crop1 = "First Crop is : " + crop1
            crop2 = "Second Crop is : " + crop2
            cform = Crops()
            return render(request,'crop.html',{'crop1':crop1,'crop2':crop2,'cform':cform})
    else:
        cform = Crops()
        return render(request,'crop.html',{'cform':cform})