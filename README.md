# Sunshine Inn Restaurant

This python code allows The Happy Cow restaurant's customers check the menu and choose what they want order from it. It is a all vegan/vegeterian restaurant.

## Features:

- It starts by welcoming the user and asking them their name:

![name](/images/NameInput.png)

- The user has two options of menus:

![mainMenu](/images/mainMenu.png)

- After chossing from the two option the menu with the different dishes is display. Each of the dishes has discription, calories and cooking time:

![saladMenu](/images/saladMenu.png)

- Every time the user is choosing a dish, it is printed to the terminal:

![dishPrinted](/images/dishPrinted.png)

- Users can decide whether to finish their order or prefer to continue ordering. They can see the complete order:

![completeOrder](/images/completeOrder.png)

- Once user finish they order, the order worksheet is updated and this way the cook can see the name of the customer and every dish they have ordered :

![orderUpdated](/images/ordersUpdated.png)

## Input validation:
- Users must provide a valid name
- There is one input that only accepts the words Salad, Pizza, or Burger
- The rest of the input accepts only integers within the range


## Testing
I have manually tested this project by doing:
- Pased the code throught a PEP8 only with one warning 
- Given invalid inputs: string where numbers are expected, numbers where strings are expected, out of range inputs
- Tested in the local terminal and the Code Institute Heroku terminal

## Bugs
### Solved Bugs:
- When I was writing the code I was not able to update the orders worksheet: I was having a error message every time. This was because I was trying to append a two dimensional list. Using a different method (insert_rows) I was able to update the worksheet
- The creds.json file was dissapearing every time I was closing the workspace. I had to create a new repository to fix the problem. Because of this there are not enough commits

## Validator testing:
- I got this warning when I run the code in PEP8 validator:
![PEP8:](/images/PEP8.png)
After check my code a few times I could not find a better way to write that part of the code.

## Deployment 

This project was deployed using personal Heroku account.

Steps for deployment:

- Fork or clone this repository
- Create a new Heroku app
- Set the builtpacks to Python and NodeJS in the order
- Link the Heroku app to repository
- Click on Deploy


## Credits

- Code institute for provide the template.
- Clarifying concepts with w3schools.com and https://pythontutor.com/.
- I want to give credits to my tutor Sandeep Aggarwal.
- The README sample was taken from Battleship Game Project. 

