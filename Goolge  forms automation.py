from selenium import webdriver
browser = webdriver.Chrome("D:/Ramón/Descargas/chromedriver.exe")
option = webdriver.ChromeOptions()
option.add_argument("-incognito")
import time 
time.sleep(1)
#get page:
browser.get('https://docs.google.com/forms/d/e/1FAIpQLSfVPAs1ZZJkfYaDs0CQHBDE5PbDm8cEmdTgDT5I48RheKUKIQ/viewform')

#classes 

textbox = browser.find_elements_by_class_name('quantumWizTextinputPaperinputInput')
radiobuttoms = browser.find_elements_by_class_name('appsMaterialWizToggleRadiogroupOffRadio')
checkbox = browser.find_elements_by_class_name('quantumWizTogglePapercheckboxInnerBox')
submittbuttom = browser.find_elements_by_class_name('appsMaterialWizButtonPaperbuttonLabel')

#respuesta 1: edad
import random
p_edad = str(random.randint(16,70))
time.sleep(1)
edad = textbox[0].send_keys(p_edad)

#resuesta 2: sexo
time.sleep(1)
random_number_prob = random.randrange(0,100)
if random_number_prob < 50:
    radiobuttoms[0].click()
else:
    radiobuttoms[1].click()
time.sleep(1)
#respuesta 3: numero de libros que compra
numero_libros_edadbaja = str(random.randint(0,20))
numero_libros_edadalta = str(random.randint(1,50))
if p_edad < str(20):
    textbox[1].send_keys(numero_libros_edadbaja)
elif p_edad > str(20):
    textbox[1].send_keys(numero_libros_edadalta)

time.sleep(1)
#respuesta 4: precio medio libros
if numero_libros_edadbaja == str(0):
    textbox[2].send_keys(0)
elif p_edad < str(20) and numero_libros_edadbaja < str(10):
    textbox[2].send_keys((random.randrange(10,20,5)))
elif p_edad < str(20) and numero_libros_edadbaja > str(10):
    textbox[2].send_keys((random.randrange(10,15,5)))
elif p_edad > str(20) and numero_libros_edadalta < str(25):
    textbox[2].send_keys((random.randrange(5,50,5)))
elif p_edad > str(20) and numero_libros_edadalta > str(25):
    textbox[2].send_keys((random.randrange(5,30,5)))
#respuesta 5: horas de ocio
time.sleep(1)
textbox[3].send_keys((random.randrange(5,48,3)))

#respuesta 6: soporte de lectura
time.sleep(1)
if random_number_prob < 33:
    radiobuttoms[2].click()
elif random_number_prob > 33:
    radiobuttoms[3].click()
elif random_number_prob >= 66:
    radiobuttoms[4].click()

#respuesta 7: tematica
tematica = [0,1,2,3,4,5,6,7]
numtematicas = random.choices(tematica,k = random.randint(1,5))
p_tematicalibros_sociales = browser.find_element_by_xpath('//*[@id="i45"]/div[2]')
p_tematicalibros_tecnologico = browser.find_element_by_xpath('//*[@id="i48"]/div[2]')
p_tematicalibros_naturales = browser.find_element_by_xpath('//*[@id="i51"]')
p_tematicalibros_humanas = browser.find_element_by_xpath('//*[@id="i54"]/div[2]')
p_tematicalibros_historia = browser.find_element_by_xpath('//*[@id="i57"]/div[2]')
p_tematicalibros_novela = browser.find_element_by_xpath('//*[@id="i60"]/div[2]')
p_tematicalibros_fantasia = browser.find_element_by_xpath('//*[@id="i63"]/div[2]')
p_tematicalibros_otras = browser.find_element_by_xpath('//*[@id="i66"]/div[2]')
tematica = [p_tematicalibros_sociales,p_tematicalibros_tecnologico,p_tematicalibros_naturales,p_tematicalibros_humanas,p_tematicalibros_historia,p_tematicalibros_novela,p_tematicalibros_fantasia,p_tematicalibros_otras]
numerodetematicas = len(numtematicas)
randomchoose = random.choices(tematica,k = numerodetematicas)
time.sleep(1)
if numerodetematicas == 1:
    randomchoose[0].click()
elif numerodetematicas == 2:
    randomchoose[0].click()
    randomchoose[1].click()
elif numerodetematicas == 3:
    randomchoose[0].click()
    randomchoose[1].click()
    randomchoose[2].click()
elif numerodetematicas == 4:
    randomchoose[0].click()
    randomchoose[1].click()
    randomchoose[2].click()
    randomchoose[3].click()
elif numerodetematicas == 5:
    randomchoose[0].click()
    randomchoose[1].click()
    randomchoose[2].click()
    randomchoose[3].click()
    randomchoose[4].click()

#respuesta 8: media numero paginas de los libros:

prob_pagslibros = [0,1,2,3,4,5,6,8]
randomchoose = random.choice(prob_pagslibros)
print ('pick is equal to: ' + 'prob_pagslibros')
time.sleep(1)
if randomchoose == 0:
    radiobuttoms[5].click()
elif randomchoose == 1:
    radiobuttoms[6].click()
elif randomchoose == 2:
    radiobuttoms[7].click()
elif randomchoose == 3:
    radiobuttoms[8].click()
elif randomchoose == 4:
    radiobuttoms[9].click()
elif randomchoose == 5:
    radiobuttoms[10].click()
elif randomchoose == 6:
    radiobuttoms[11].click()
elif randomchoose == 7:
    radiobuttoms[12].click()
elif randomchoose == 8:
    radiobuttoms[13].click()

#respuesta 9: velocidad de lectura

if randomchoose == 0:
    radiobuttoms[14].click()
elif randomchoose == 1:
    radiobuttoms[15].click()
elif randomchoose == 2:
    radiobuttoms[16].click()
elif randomchoose == 3:
    radiobuttoms[17].click()
elif randomchoose == 4:
    radiobuttoms[18].click()
elif randomchoose == 5:
    radiobuttoms[19].click()

#respuesta 10: Nivel de estudios 
if randomchoose == 0:
    radiobuttoms[20].click()
elif randomchoose == 1:
    radiobuttoms[21].click()
elif randomchoose == 2:
    radiobuttoms[22].click()
elif randomchoose == 3:
    radiobuttoms[23].click()
elif randomchoose == 4:
    radiobuttoms[24].click()
elif randomchoose == 5:
    radiobuttoms[25].click()
#respuesta 11: Ocupación

#lista ocupacion
ocupacion = [0,1,2] #otro se añade si p_ocupacion is True
randomocupacion = random.choice(ocupacion)
time.sleep(1)
if randomocupacion == 0:
    checkbox[8].click()
elif randomocupacion == 1:
    checkbox[9].click()
elif randomocupacion == 2:
    checkbox[10].click()

#Enviar encuesta:
submittbuttom[0].click()

browser.close()




