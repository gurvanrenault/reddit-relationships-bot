# This file contain all the functions for social analysis  ( gender ,cliches, age , subject  ... ) posted in /r/relationships/
import os
from settings import SETTINGS
cliches = [
    {
        "advice": "Break up",
        "spellings": ["divorce", "break up", "leave him", "leave her"],
        "comments": [],
    },
    {
        "advice": "Get your ducks in a row",
        "spellings": ["ducks in a row"],
        "comments": [],
    },
    {
        "advice": "Don't JADE",
        "spellings": ["jade"],
        "comments": [],
    },
    {
        "advice": "Grey rock",
        "spellings": ["grey rock", "grey-rock", "gray rock", "gray-rock"],
        "comments": [],
    },
    {
        "advice": "Consult a lawyer",
        "spellings": ["lawyer"],
        "comments": [],
    },
    {
        "advice": "Go no-contact",
        "spellings": ["no contact", "no-contact"],
        "comments": [],
    },
    {
        "advice": "Love languages",
        "spellings": ["love language"],
        "comments": [],
    },
    {
        "advice": "Low-contact",
        "spellings": ["low contact", "low-contact"],
        "comments": [],
    },
    {
        "advice": "\"No\" is a complete sentence",
        "spellings": ["no is a complete sentence", "\"no\" is a complete sentence"],
        "comments": [],
    },
    {
        "advice": "Red flag",
        "spellings": ["red flag"],
        "comments": [],
    },
    {
        "advice": "Get therapy / counselling",
        "spellings": ["therapy", "counselling"],
        "comments": [],
    },
    {
        "advice": "Hit the gym",
        "spellings": ["hit the gym", "go the the gym", "going to the gym"],
        "comments": [],
    },
    {
        "advice": "Narcissist",
        "spellings": ["narcissist", "narcisist", "narcissism", "narcisism"],
        "comments": [],
    },
]


def display_information(comments_analysed, submissions_analysed):
    os.system('cls' if os.name == 'nt' else 'clear')
    print "Analysing %d submissions for cliches" % (SETTINGS["SUBMISSIONS_TO_ANALYSE"])
    print "Analysed %d comments from %s submissions\n" % (comments_analysed, submissions_analysed + 1)
    for cliche in cliches:
        print "%s: %s" % (cliche['advice'], len(cliche['comments']))
    print ('\n');

def analyse_comment(comment):
    for cliche in cliches:
        for spelling in cliche['spellings']:
            if hasattr(comment, 'body') and spelling in comment.body.lower():
                cliche['comments'].append(comment.id)

def is_OP(div_id,sliped_post):
    # Check if the formatted string is about the Original Poster
    op_marker=["me","i","myself","my"];
    if (sliped_post[div_id-1].lower() in op_marker):
        return True;
    return False;

def analyse_gender_OP(post,men,women,tot_gender):
    # Analyse the gender of the Original Poster
    gender=False;
    open_brackets=["[","("];
    end_brackets=["]",")"];
  
    post_splitted=post.split(" ")
    for div_id in range(0,len(post_splitted)-1):
    
        if ((post_splitted[div_id][0] in open_brackets)and (post_splitted[div_id][len(post_splitted[div_id])-1]in end_brackets)and is_OP(div_id,post_splitted) ):
           #  If the format look like [42F] or (42F)  
            if (post_splitted[div_id].count("f")!=0 or  post_splitted[div_id].count("F")!=0):
                # OP is a women
                women=women+1;
                tot_gender=tot_gender+1;
            if (post_splitted[div_id].count("m")!=0 or  post_splitted[div_id].count("M")!=0):
                #OP is a men
                men=men+1
                tot_gender=tot_gender+1;
    return ( men,women,tot_gender);

def  display_analyse_gender_OP(men,women,total):
    print "Analysing the gender of originals posters .."
    print "%s: %s" % ("Percentage of OP  men ",( (men*1.0)/total)*100) +'%'
    print "%s: %s " % ("Percentage of OP  women " , ( (women*1.0)/total)*100) +'%'


               
             
