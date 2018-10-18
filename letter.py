def write_letter(position, company):
    # Creates the letter
    base_letter = '''Jake Reck
(860) 933-0862
jakereck@gmail.com

Dear Whomever it may concern,

    Hi! My name is Jake Reck. My goal in life is to either be the antagonist
or protagonist in Elon Musk's rise to power. But, for the time being, I will 
settle on being the every-day software developer.

    I would be a perfect fit for the {position} position at {company}. 
I have been teaching myself software development over the last 3 years, 
but my passion for programming started many years ago when I was a 
sophmore in high school and took my first C++ class. 

My passion was sparked again when I moved out to Washington state and was looking
for ways to make some extra cash. My journey started out in web development languages;
HTML, CSS, JavaScript, and jQuery. As time went on I hardened my skills as a web developer
doing freelance projects and projects for friends and family. I also dove deeper into other
languages such as Python, C#, Ruby (Rails), and other web frameworks.

Since there, I have continued down the rabbit-hole and started expanding my skills in other
programming avenues. I ended up settling my focus on the Python language, not only for its ease,
but also its strength and power to do just about anything! This cover letter was even 
automated by a Python program I wrote - check it out at https://github.com/Jereck/cover-letter-generate
I have also been using Machine Learning in my currrent career just for fun to automate 
ABC (Antecedent - Behavior - Consequence) data.

I would love to talk with you in person about my soft skills as a team player, self-motivator, 


I look forward to hearing from you,
    Jake Reck
    '''.format(position=position, company=company)

    filename = r'C:\Users\jaker\Desktop\coverletters\{company}.doc'.format(company=company)
    f = open(filename, 'w')
    f.write(base_letter)
    f.close()