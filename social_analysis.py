# This file contain all the functions for social analysis  ( gender , age , subject  ... ) posted in /r/relationships/

def is_OP(div_id,sliped_post):
    # Check if the formatted string is about the Original Poster
    op_marker=["me","i","myself","my"];
    if (sliped_post[div_id-1].lower() in op_marker):
        return True;
    return False;

def analyse_gender_OP(post,man,women,tot_gender):
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
                man=man+1
                tot_gender=tot_gender+1;
    return ( man,women,tot_gender);

def  display_analyse_gender_OP(man,women,total):
    print "Analysing the gender of originals posters .."
    print "%s: %s" % ("Percentage of OP  men ",( (man*1.0)/total)*100) +'%'
    print "%s: %s " % ("Percentage of OP  women " , ( (women*1.0)/total)*100) +'%'


               
             
