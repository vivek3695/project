import random
A=''
sec1=0
sec2=0
sec3=0
sec4=0
sec5=0
a1=("India is a federal union comprising twenty-nine states and how many union territories?")
a2=("Which of the following is the capital of Arunachal Pradesh?")
a3=("What are the major languages spoken in Andhra Pradesh?")
a4=("What is the state flower of Haryana?")
a5=("Which of the following states is not located in the North?")
a6=("In which state is the main language Khasi?")
a7=("Which is the largest coffee producing state of India?")
a8=("Which state has the largest area?")
a9=("Which state has the largest population?")
a10=("In what state is the Elephant Falls located?")
b1=("What is the southern most part of India called?") 
b2=("Which Bridge in India is actually highest bridge of world?")
b3=("Which place in India is second coldest place in world?")
b4=("Which place in India is wettest place in world?")
b5=("The biggest desert of India-Thar in Rajasthan is ……………largest in World.")
b6=("Which is the biggest city in India area wise?")
b7=("Which is the biggest waterfalls in India?")
b8=("Which river is known as Ganga of South?")
b9=("Kanchenjunga is the highest mountain peak in India. What is its position in World?")
b10=("Which of the following states of India does not share a boundary with Myanmar?")
c1=("The dance encouraged and performed from the temple of Tanjore was")
c2=("Natya Shastra the main source of India classical dances was written by")
c3=("The sacred book of the Parsis is called")
c4=("The last Mahakumbh of the 20th Century was held at")
c5=("Koodiyattam is a")
c6=("The national song of India was composed by")
c7=("The headquarters of the Sahitya Akademi is at")
c8=("The ratio of width of our National flag to its length is")
c9=("Kathakali is a folk dance prevalent in which state ?")
c10=("The words ‘Satyameva Jayate’ inscribed below the base plate of the emblem of India are taken from")
d1=("Gurpurab, the festival of the guru, is celebrated by people of which religion?")
d2=("On 21st March, people of which religion celebrate Navroz as their new year?")
d3=("Bihu, the harvest festival, is celebrated in which state of India?")
d4=("Which festival is celebrated as harvest festival in North India?")
d5=("Which of the following is not a harvest festival?")
d6=("In which festival, Lakshmi, the goddess of wealth, is worshipped")
d7=("In which festival birth of Jesus Christ is celebrated?")
d8=("The festival Muharram is celebrated by people of which religion?")
d9=("In which state of India, Chatth Puja is prominently celebrated?")
d10=("Which city hosts the Kala Ghoda Art festival in February every year?") 
e1=("Which of the following freedom fighters was also a civil rights activist in South Africa")
e2=("Which of the following freedom fighters is also known as the Unofficial Ambassador of India")
e3=("Who was the founder of Jugantar?")
e4=("Who among the following was arrested for leading the Alipore bomb Conspiracy")
e5=("What was Motilal Nehru's profession?")
e6=("Who was called the Father of the Indian Unrest by the British?")
e7=("Which viceroy is regarded as the catalyst of Indian nationalism?")
e8=("Gopal Krishna Gokhale founded")
e9=("Who had chaired the Indian Education Commission in 1882?")
e10=("Annie Besant is mostly associated with")
l1=[a1,a2,a3,a4,a5,a6,a7,a8,a9,a10]
l2=[b1,b2,b3,b4,b5,b6,b7,b8,b9,b10]
l3=[c1,c2,c3,c4,c5,c6,c7,c8,c9,c10]
l4=[d1,d2,d3,d4,d5,d6,d7,d8,d9,d10]
l5=[e1,e2,e3,e4,e5,e6,e7,e8,e9,e10]
print("welcome to the quiz")
print ("this quiz contains 5 different sections") 
print("you can attempt each level only once") 
print("after attempting all five levels your score will be displayed")
G=int(input('enter a no'))
if G==1:
    x=input("to proceed with section-1 press enter")
    Z=print("SECTION 1: INDIAN AND ITS STATES")
    for i in range(10):    
        if x==A:    
            print("enter your CHOICE") 
            y=random.choice(l1)
            if y==a1:
                print(a1)
                z=int(input('1-6, 2-7, 3-8, 4-9 : '))
                if z==2:
                    print("correct")
                    sec1=sec1+1
                else:
                    print("wrong")
                l1.remove(y)    

            elif y==a2:
                  print(a2)
                  z=int(input("1-ITANAGAR, 2-DISPUR, 3-IMPHAL, 4-PANAJI : "))
                  if z==1:
                      print("correct")
                      sec1=sec1+1
                  else:
                      print("wrong")
                  l1.remove(y) 
            elif y==a3:
                  print(a3)
                  z=int(input('1-ENGLISH AND TELUGU, 2-TELUGU AND URDU 3-TELUGU AND KANADA 4-ALL OF THE ABOVE LANGUAGES : '))
                  if z==2:
                      print("correct")
                      sec1=sec1+1
                  else:
                      print("wrong")
                  l1.remove(y)
            elif y==a4:
                  print(a4)
                  z=int(input("1-LOTUS , 2-RHODODENDRON, 3-GOLDEN SHOWER, 4-NOT DECLARED : "))
                  if z==1:
                      print("correct")
                      sec1=sec1+1
                  else:
                      print("wrong")
                  l1.remove(y)    
            elif y==a5:
                  print(a5)
                  z=int(input("1-JHARKHAND , 2-JAMMU AND KASHMIR, 3-HIMACHAL PRADESH , 4-HARYANA : "))
                  if z==1:
                      print("correct")
                      sec1=sec1+1
                  else:
                      print("wrong")
                  l1.remove(y)
            elif y==a6:
                  print(a6)
                  z=int(input("1-MIZORAM ,2-NAGALAND ,3-MEGHALAYA, 4-TRIPURA: "))
                  if z==3:
                      print("correct")
                      sec1=sec1+1
                  else:
                      print("wrong")
                  l1.remove(y)
            elif y==a7:
                  print(a7)
                  z=int(input("1-KERALA , 2-TAMIL NADU , 3-KARNATAKA , 4-ARUNACHAL PRADESH"))
                  if z==3:
                      print("correct")
                      sec1=sec1+1
                  else:
                      print("wrong")
                  l1.remove(y)
            elif y==a8:
                  print(a8)
                  z=int(input("1-MAHARASHTRA, 2-MADHYA PRADESH, 3-UTTAR PRADESH, 4-RAJASTHAN"))
                  if z==4:
                      print("correct")
                      sec1=sec1+1
                  else:
                      print("wrong")
                  l1.remove(y)
            elif y==a9:
                  print(a9)
                  z=int(input('1-UTTAR PRADESH , 2-MAHARASTRA , 3-BIHAR , 4-ANDHRA PRADESH : '))
                  if z==1:
                      print("correct")
                      sec1=sec1+1
                  else:
                      print("wrong")
                  l1.remove(y)
            elif y==a10:
                  print(a10)
                  z=int(input('1-MIZORUM , 2-ORISSA, 3-MANIPUR, 4-MEGHALAYA : '))
                  if z==4:
                      print("correct")
                      sec1=sec1+1
                  else:
                      print("wrong")
                  l1.remove(y)
    print('your score is',sec1)              
elif G==2:
    x=input("to proceed with section-2 press enter: ")
    Z=print("SECTION 2: INDIAN GEOGRAPHY")
    for i in range(10):
        if x==A:
            print("enter your CHOICE") 
            y=random.choice(l2)
            if y==b1:
                print(b1)
                z=int(input('1-JAWAHAR POINT, 2-ANNA POINT, 3-INDRA POINT, 4-ANDAMAN POINT : '))
                if z==3:
                    print("correct")
                    sec2=sec2+1
                else:
                    print("wrong")
                l2.remove(y)    
            elif y==b2:
                  print(b2)
                  z=int(input("1-BAILEY BRIDGE, 2-SUKAN BRIDGE, 3-HOWRAH BRIDGE, 4-JAWAR BRIDGE : "))
                  if z==1:
                      print("correct")
                      sec2=sec2+1
                  else:
                      print("wrong")
                  l2.remove(y) 
            elif y==b3:
                  print(b3)
                  z=int(input('1-DRASS, 2-KASHMIR, 3-TWANG, 4-NONE : '))
                  if z==1:
                      print("correct")
                      sec2=sec2+1
                  else:
                      print("wrong")
                  l2.remove(y)
            elif y==b4:
                  print(b4)
                  z=int(input("1-CHERAPUNJI , 2-MAWSYNRAM, 3-KOCHI, 4-NICOBAR ISLAND: "))
                  if z==2:
                      print("correct")
                      sec2=sec2+1
                  else:
                      print("wrong")
                  l2.remove(y)    
            elif y==b5:
                  print(b5)
                  z=int(input("1-3rd , 2-4th, 3-6th, 4-7th : "))
                  if z==4:
                      print("correct")
                      sec2=sec2+1
                  else:
                      print("wrong")
                  l2.remove(y)
            elif y==b6:
                  print(b6)
                  z=int(input("1-MUMBAI ,2-KOLKATA ,3-CHENNAI, 4-DELHI: "))
                  if z==2:
                      print("correct")
                      sec2=sec2+1
                  else:
                      print("wrong")
                  l2.remove(y)
            elif y==b7:
                  print(b7)
                  z=int(input("1-KUNTALA FALLS , 2-JOG FALLS, 3-TALALONA , 4-RAJRAPPA: "))
                  if z==2:
                      print("correct")
                      sec2=sec2+1
                  else:
                      print("wrong")
                  l2.remove(y)
            elif y==b8:
                  print(b8)
                  z=int(input("1-GODAVARI, 2-TUNGABADRA, 3-NARMADA, 4-PAMBA "))
                  if z==1:
                      print("correct")
                      sec2=sec2+1
                  else:
                      print("wrong")
                  l2.remove(y)
            elif y==b9:
                  print(b9)
                  z=int(input('1-2, 2-3 , 3-4 , 4-5 : '))
                  if z==2:
                      print("correct")
                      sec2=sec2+1
                  else:
                      print("wrong")
                  l2.remove(y)
            elif y==b10:
                  print(b10)
                  z=int(input('1-ARUNACHAL PRADESH, 2-MANIPUR, 3-NAGALAND, 4-ASSAM : '))
                  if z==4:
                      print("correct")
                      sec2=sec2+1
                  else:
                      print("wrong")
                  l2.remove(y)
    print('your score is',sec2)              
elif G==3:
      x=input("to proceed with section-3 press enter")
      Z=print("SECTION 3:ARTS AND CULTURE ")
      for i in range(10):    
          if x==A:    
              print("enter your CHOICE") 
              y=random.choice(l3)
              if y==c1:
                  print(c1)
                  z=int(input('1-BHARATNATYAM, 2-KATHAKALI, 3-ODISSI, 4-MOHINIATTAM : '))
                  if z==1:
                      print("correct")
                      sec3=sec3+1
                  else:
                      print("wrong")
                  l3.remove(y)    

              elif y==c2:
                    print(c2)
                    z=int(input("1-BHARAT MUNI, 2-TANDU MUNI, 3-NARAD MUNI, 4-ABHINAV GUPT : "))
                    if z==1:
                        print("correct")
                        sec3=sec3+1
                    else:
                        print("wrong")
                    l2.remove(y) 
              elif y==c3:
                    print(c3)
                    z=int(input('1-TORAH, 2-BIBLE, 3-GITA, 4-ZEND AVESTA: '))
                    if z==4:
                        print("correct")
                        sec3=sec3+1
                    else:
                        print("wrong")
                    l3.remove(y)
              elif y==c4:
                    print(c4)
                    z=int(input("1-HARIDWAR , 2-NASIK, 3-UJJAIN, 4-ALLAHABAD: "))
                    if z==1:
                        print("correct")
                        sec3=sec3+1
                    else:
                        print("wrong")
                    l3.remove(y)    
              elif y==c5:
                    print(c5)
                    z=int(input("1-DRESS PREPARE IN GOA , 2-TRADITIONAL DANCE OF KERALA, 3-FESTIVAL OF ANDHRA PRADESH, 4-NONE : "))
                    if z==2:
                        print("correct")
                        sec3=sec3+1
                    else:
                        print("wrong")
                    l3.remove(y)
              elif y==c6:
                    print(c6)
                    z=int(input("1-IQUBAL ,2-RABINDRANATH TOGORE ,3-JAI SHANKAR PRASAD, 4-BHANKIM CHANDRA CHATTERJI: "))
                    if z==4:
                        print("correct")
                        sec3=sec3+1
                    else:
                        print("wrong")
                    l3.remove(y)
              elif y==c7:
                    print(c7)
                    z=int(input("1-MUMBAI , 2-CHANNAI, 3-NEW DELHI , 4-KOLKATA "))
                    if z==3:
                        print("correct")
                        sec3=sec3+1
                    else:
                        print("wrong")
                    l3.remove(y)
              elif y==c8:
                    print(c8)
                    z=int(input("1-2:4, 2-3:4, 3-2:3, 4-3:4 "))
                    if z==3:
                        print("correct")
                        sec3=sec3+1
                    else:
                        print("wrong")
                    l3.remove(y)
              elif y==c9:
                    print(c9)
                    z=int(input('1-ORRISA, 2-MANIPUR , 3-KARNATAKA , 4-KERALA: '))
                    if z==4:
                        print("correct")
                        sec3=sec3+1
                    else:
                        print("wrong")
                    l3.remove(y)
              elif y==c10:
                    print(c10)
                    z=int(input('1-RAMAYANA, 2-MUNDAK UPANISHAD, 3-RIGVEDA, 4-SAPATH BRAHMANA : '))
                    if z==2:
                        print("correct")
                        sec3=sec3+1
                    else:
                        print("wrong")
                    l3.remove(y)
    print('your score is',sec3)
elif G==4:
    print(a1)



    
