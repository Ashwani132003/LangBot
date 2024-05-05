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
        return payment_url

    st.title('Show your Support!!')
    st.write('(Only for teaching, no real money transfer using this link )')
    if global_state.email:
        # if st.button('Donate'):
        url = click()
        st.markdown(f'<a href="{url}" target="_blank" style="background-color: #008CBA; color: white; padding: 10px 20px; text-align: center; text-decoration: none; display: inline-block; border-radius: 4px;">Donate</a>', unsafe_allow_html=True)
            # click()
    else:
        st.write('Please Login to be eligible for Stripe Payment!')        

    st.markdown('')
    st.markdown('')
    st.markdown('')
    st.markdown('')

    st.write("Buy me a coffee! (For actually showing your support!! Real money will be deducted)")
    url ='https://buymeacoffee.com/beginnerscodezone'

    st.markdown(f'<a href="{url}" target="_blank" style="background-color: #008CBA; color: white; padding: 10px 20px; text-align: center; text-decoration: none; display: inline-block; border-radius: 4px;">Donate</a>', unsafe_allow_html=True)


app()