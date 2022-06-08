# Sunshine Inn Restaurant

This python code allows Sunshine Inns restaurant's customer check the menu and choose what they want order from it. It is a all vegan/vegeterian restaurant.

## Features:

- It starts by welcoming the user and asking them which menu they would prefer: Vegan or Vegeterian;
[screenshot]

- After chossing from the two option of menu and specific menu is display:
[screenshot]

- User can see all the dishes  they have between Salad, Pizza or Burgers. Each of the dishes has discription, calories and cooking time.
[screenshot]

- Users can say if they finish they order or if they prefer to keep ordering:
[screenshot]

- Once user finish they order, the order worksheet is updated and this way the cook can see the name of the customer and every dish they have ordered 
[screenshot]

## Input validation:
-Users must provide a valid name
-There is one input that only accepts the words Salad, Pizza, or Burger
-The rest of the input accepts only integers within the range


## Testing
I have manually tested this project by doing:
- Pased the code throught a PEP8 
- Given invalid inputs: string where numbers are expected, numbers where strings are expected, out of range inputs
- Tested in the local terminal and the Code Institute Heroku terminal

## Bugs
-When I was writing the code I was not able to update the orders worksheet: I was having a error message every time. This was because I was trying to append a two dimensional list. Using a different method (insert_rows) I was able to update the worksheet

- The creds.json file was dissapearing every time I was closing the workspace. I had to create a new repository to fix the problem. Because of this there are not enough commits
- Every time I was opening the workspace I had to install gspread and tabulate modules. I fixed it typing this two modules in the requirements.txt files

## Validator testing:
- I got this warning when I run the code in PEP8 validator:
![PEP8:](/images/PEP8.png)
After check my code a few times I could not find the way to change the code lines and fix it. 

## Deployment 