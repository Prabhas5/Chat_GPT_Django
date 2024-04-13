from django.shortcuts import render
import openai
from .forms import CandidateResponseForm

def evaluate_candidate(request):
    if request.method == 'POST':
        # Get user responses from the form
        position_applied=request.POST.get("position_applied")
        about_myself=request.POST.get("about_myself")
        experience = request.POST.get('experience')
        experience_years = request.POST.get('experience_years')
        ans1 = request.POST.get('ans1')
        ans2 = request.POST.get('ans2')
        ans3 = request.POST.get('ans3')
        ans4 = request.POST.get('ans4')
        ans5 = request.POST.get('ans5')
        ans6 = request.POST.get('ans6')
        ans7 = request.POST.get('ans7')
        ans8 = request.POST.get('ans8')
        ans9 = request.POST.get('ans9')
        ans10 = request.POST.get('ans10')
        
        # Construct prompt for ChatGPT
        prompt = f"""
        Context: Act as HR Interviewer & Analyst

        Prompt: I have received the questionnaire responses from a candidate applying for the position of Manager.

        Based on their responses, please help me evaluate their qualification for the role by classifying them as either QUALIFIED, SOMEWHAT QUALIFIED, or NOT QUALIFIED.

        The evaluation should take into account their skills, communication abilities, experience & intelligence. Here are the candidate’s responses to the questionnaire:

        Position Applied: {position_applied}

        Role: Manager

        About Myself: {about_myself}

        Experience: {experience} {experience_years}

        Q1 - Can you describe your experience with diary management and scheduling appointments?
        A1 - {ans1}

        Q2 - How do you handle confidential information and sensitive situations?
        A2 - {ans2}

        Q3 - Can you provide an example of a complex problem you've solved in a similar role?
        A3 - {ans3}

        Q4 - How do you prioritize tasks and manage your time when dealing with a busy executive's schedule?
        A4 - {ans4}

        Q5 - How comfortable are you with liaising with high-level stakeholders and managing professional relationships?
        A5 - {ans5}

        Q6 - Can you describe a situation where you had to handle an unexpected issue or emergency?
        A6 - {ans6}

        Q7 - What experience do you have with travel planning and logistics?
        A7 - {ans7}

        Q8 - How do you ensure effective communication between the MD and other parties?
        A8 - {ans8}

        Q9 - Can you provide an example of an initiative you took to improve efficiency or effectiveness in your role?
        A9 - {ans9}

        Q10 - How do you handle stress and pressure in managing a busy executive's affairs?
        A10 - {ans10}
        """    
        #Query ChatGPT for evaluation
        Api_key='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'
        client=openai.OpenAI(api_key=Api_key)
        chat_completion = client.chat.completions.create(
        messages=[
            {
            "role": "user",
            "content": prompt,
            }
                ],
            model="gpt-3.5-turbo",
            temperature=0.5,
            max_tokens=150,
            n=1,
            stop=["\n"]
             )

        # Get the AI-generated response
        print("------------------------------------------------------------------------")
        ai_response = chat_completion.choices[0].message.content
        #saving the form to database
        form = CandidateResponseForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'gpt/analyse.html',{"ai_response":ai_response})        
    form=CandidateResponseForm()
    return render(request, 'gpt/home.html',{"form":form})
