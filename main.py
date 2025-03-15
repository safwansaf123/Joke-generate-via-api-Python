import streamlit as safoo    # Importing streamlit module to create web app
import requests as req       # Importing requests module to make API calls to the server

def get_random_joke():
    '''fetch random joke from the API'''
    try:   # Try to make a GET request to the API
        response = req.get("https://official-joke-api.appspot.com/random_joke") # Making a GET request to the API just check on web browser
        if response.status_code == 200: # If the response is successful (status code 200) then store the joke data
            joke_data = response.json() # Storing the joke data in JSON format in joke_data variable
            return f"{joke_data['setup']}\n\n{joke_data['punchline']}" # Returning the joke data
        else: # If the response is not successful then return the error message, unable to fetch the joke data from api
            return "Error: Unable to fetch the joke data from the API"   
        
    except: # If there is an exception then return the error message
        return "Error: Unable to fetch the joke data due other reason like network issue"
    
def main():
    '''Main function to create the web app'''
    safoo.title("Random Joke Generator") # Setting the title of the web  app heading
    safoo.write("Click the button below to get a random joke") # Displaying the message on the web app
    if safoo.button("Get Random Joke"): # Creating a button on the web app
        joke = get_random_joke() # Fetching the random joke from the API by calling the get_random_joke function from above
        safoo.success(joke) # Displaying the joke on the web app in green colour 
        

        safoo.divider() # Creating a divider on the web app to separate the widgets by thin line
        safoo.markdown("LEARN WITH ASHARIB ALI, BY SAFWAN AHMED ") # Displaying the message on the web app
        # Displaying the message on the web app by applying the HTML tags to the text or CSS
        safoo.markdown("""
        <div style="display:flex; justify-content:center; align-items:center; margin-top:20px;">
        <p>Follow me on:   </p>
        <P> <a href="https://www.facebook.com/safwan.ahmed.777">   LinkedIn</a> </p>         
                                      </div>"""
        , unsafe_allow_html=True) 
                            

if __name__ == "__main__": # Checking if the script is run directly
    main() # Calling the main function to create the web app    