import streamlit as st
import stripe
import urllib.parse
import webbrowser

from firebase_admin import credentials, initialize_app, storage, firestore
import firebase_admin
from src.main import global_state


        

def app():

        
    def get_link(customer):
        
                    
        session = stripe.checkout.Session.create(
            customer=customer.id,
            payment_method_types=['card'],
            line_items=[{
                'price':st.secrets['price_key'], #test
                'quantity': 1,
            }],
            mode='payment',
            success_url=st.secrets['redirect_url'],
            # success_url=st.secrets['redirect_url'],
            cancel_url=st.secrets['redirect_url'],

            metadata = {
                'payment type': 'monthly',
            },
        )

        #url=f"{stripe_link}?prefilled_email={encoded_email}"
        return session.url

    def click():    
        email=global_state.email
        stripe.api_key = st.secrets['stripe_api_key']

        customers = stripe.Customer.list(email=email)
        
        if customers.data:
            customer = customers.data[0]
        else:
            customer = stripe.Customer.create(email=email)


        payment_url=get_link(customer)  
        print(payment_url)                 
        webbrowser.open(payment_url)

    st.title('Show your Support!!')
    if global_state.email:
        if st.button('Donate'):
            click()
    else:
        st.write('Please Login to be eligible for Payment!')        



app()