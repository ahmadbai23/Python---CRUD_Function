# Capstone Project Modul 1
Please read this before you proceed to run the application

This Python project was created to fulfill the Capstone Project Module 1, which involves the implementation of fundamental Python learning from the Digital Science course by Purwadhika Digital School. This application was created to apply the functions of CRUD Data. The data used is dummy data that is not connected to a database. This application is purely a programming exercise aimed at understanding the fundamental usage of Python.

In this application, I am using 2 libraries: tabulate and pyinputplus.

* Tabulate: This library is used for visualizing tables. It helps in displaying data in a tabular format, making it easier to read and understand.
* PyInputPlus: This library is used for input validation. It provides functions to take user input while validating and handling various types of input errors, such as invalid input or wrong data types. This ensures that the user input is accurate and appropriate for the application's requirements. <br />
![Alt text](https://github.com/ahmadbai23/PythonProject/blob/main/image/library.png)

# Introduction to the App
Welcome to Bay's Rent Cars
This application is created for managing car rental data in a company, targeting the application's users as the administrators of the company.

In general, the features contained in this application are:
1. Displaying Car Data
2. Adding Car Data
3. Deleting Car Data
4. Updating Car Data

The following is an example screenshot of the main menu that will be displayed: <br />
![Alt text](https://github.com/ahmadbai23/PythonProject/blob/main/image/main_menu.png)

# Feature
## 1. Displaying Car Data
This is an implementation of the read data feature.
After the user inputs 1 to display car data, the following sub-menu read data will appear: <br />
![Alt text](https://github.com/ahmadbai23/PythonProject/blob/main/image/sub_menu_read%20data.png) <br />

Submenu 1 is used to display all the existing data. <br />
![Alt text](https://github.com/ahmadbai23/PythonProject/blob/main/image/sub_menu_read%20data_1.png) <br />
Submenu 2 displays specific data based on user input, in this case, using the car ID. <br />
![Alt text](https://github.com/ahmadbai23/PythonProject/blob/main/image/sub_menu_read%20data_2.png) <br />
Submenu 3 is used to display all data while sorting it based on the highest rental price or the lowest rental price. <br />
![Alt text](https://github.com/ahmadbai23/PythonProject/blob/main/image/sub_menu_read%20data_3.png) <br />

## 2. Adding Car Data
This is an implementation of the create data feature.
If the user chooses to add car data, they will be prompted to enter several variables needed to create that car's data.
The following is the display of the variables that the user needs to fill in: <br />
![Alt text](https://github.com/ahmadbai23/PythonProject/blob/main/image/sub_menu_create%20data.png) <br />

## 3. Deleting Car Data
This is an implementation of the delete data feature.
In this feature, the user can delete the record of the car by simply entering the Car Id that the user wants to delete.
You can only delete a single employee in one turn. <br />
![Alt text](https://github.com/ahmadbai23/PythonProject/blob/main/image/sub_menu_delete%20data.png)


## 4. Updating Car Data
This is an implementation of the update data feature.
If the user chooses the "Update Data" menu, a submenu for updating data will appear. This submenu allows you to make changes to the entire category of the car data or specific categories (e.g., only stock, price, or car model) of that car.
This functionality provides flexibility in updating either all the information related to a car or just specific attributes of the car's data.
![Alt text](https://github.com/ahmadbai23/PythonProject/blob/main/image/sub_menu_update%20data.png) <br />
If the user selects "Update Entire Data," the displayed interface will be similar to creating new data, but instead, it will modify the existing car data in the table. On the other hand, if the user chooses "Update Specific Category," they will be prompted to enter the category they want to modify and the new value for the change.
This approach allows users to update either the complete set of information for a car or focus on modifying specific attributes of the car's data, providing a more targeted updating process.
![Alt text](https://github.com/ahmadbai23/PythonProject/blob/main/image/sub_menu_update%20data_1.png) <br />

