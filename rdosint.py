import praw 
from prawcore.exceptions import NotFound,Forbidden
import datetime
import time
import os,sys 
from collections import Counter

if os.name == "nt":
   os.system("cls")
else :  
   os.system("clear")

red = "\033[1;31m"
green = "\033[1;32m"
yellow = "\033[1;33m"
pink = "\033[1;35m"
blue = "\033[1;34m"
white = "\033[1;37m"
reset = "\033[0m"

reddit = praw.Reddit(
    client_id='R2M_pIpfNt2W20BeSFtI1g',
    client_secret='uaBeAQBfloSs1A2NOqxx1TpsIL5eVw',
    user_agent='Mozilla/5.0 (iPhone; CPU iPhone OS 7_2_5; like Mac OS X) AppleWebKit/535.17 (KHTML, like Gecko)  Chrome/49.0.2503.271 Mobile Safari/534.9'
  )
print("")
banner = f"""{blue}
 █▀█ █▀▀ █▀▄ █▀▄ █ ▀█▀ {red}  █▀█ █▀ █ █▄░█ ▀█▀
{blue} █▀▄ ██▄ █▄▀ █▄▀ █ ░█░ {red}  █▄█ ▄█ █ █░▀█ ░█░
{reset}"""
print(banner)
print("")
print(f" \033[41m {white} Coder: $0ul  Github: https://github.com/zayzaymm {reset}")
print("")
username = input(f" {blue}[{green}+{blue}]{yellow} Username{green} : ")
try :
   redditor = reddit.redditor(username)
   post_karma = redditor.link_karma
except NotFound :
   print(f" {blue}[{green}*{blue}]{red} {username} doesn't exit !{reset}")
   print("")
   exit()
except Forbidden :
   print(f" {blue}[{green}*{blue}]{red} {username} is supended !{reset}")
   print("")
   exit()  
except AttributeError:
   print(f" {blue}[{green}*{blue}]{red} {username} is supended !{reset}")
   print("")
   exit()
except Exception as e:
   print(e)
   print("")
   exit()
comment_karma = redditor.comment_karma
created_date = datetime.datetime.fromtimestamp(redditor.created_utc)
posts = redditor.submissions.new(limit=None)
comments = redditor.comments.new(limit=None)
try :
   lastseen_date = datetime.datetime.fromtimestamp(list(redditor.comments.new(limit=None))[0].created_utc)
except :
   lastseen_date = created_date
total_subreddits = []
post_subreddits = []
comment_subreddits = []
file = open(f"{username}.osint","a",encoding="utf-8")
file.write("\n\n\n")
file.write(" Posts ")
file.write("\n")
file.write(" ------")
file.write("\n")
file.close() 
i = 1
x = 1
y = 1
post_count = 0
print("")
print(f"{yellow} Posted Communities{reset} ")
print(" -------------------")
print("")
for post in posts:
    if not post.subreddit.display_name in post_subreddits :
       subreddit = reddit.subreddit(post.subreddit.display_name)
       description = subreddit.public_description
       print(f" {blue}[{green}*{blue}]{yellow} Index {white}:{green} {i}{reset}")
       print(f" {blue}[{green}*{blue}]{yellow} Date & Time {white}:{green} {datetime.datetime.fromtimestamp(post.created_utc)}{reset}")
       print(f" {blue}[{green}*{blue}]{yellow} Community {white}:{green} {post.subreddit.display_name}{reset}")
       print(f" {blue}[{green}*{blue}]{yellow} Description {white}:{green} {description}{reset}")
       print("")
       post_subreddits.append(post.subreddit.display_name)
       i = i + 1
    post_count = post_count + 1 
    total_subreddits.append(post.subreddit.display_name)  
    if post_count == 1000:
       post_count = "1000+"
    post_title = post.title 
    if post.selftext :
       post_content = post.selftext
    else :
       post_content = ""
    file = open(f"{username}.osint","a",encoding="utf-8")
    file.write(f" [+] Index : {x}")
    file.write("\n")
    file.write(f" [+] Community : {post.subreddit.display_name}")
    file.write("\n")
    file.write(f" [+] Url : {post.permalink}")
    file.write("\n")
    file.write(f" [+] Date & Time : {datetime.datetime.fromtimestamp(post.created_utc)}")
    file.write("\n")
    file.write(f" [+] u/{username} : {post_title}")
    file.write("\n")
    file.write(f" [+] Body : {post.selftext}")
    file.write("\n")
    file.write(f" [+] Score : {post.score}")
    file.write("\n" + "-" * 40 + "\n")
    file.close()
    x = x + 1
file = open(f"{username}.osint","a",encoding="utf-8")
file.write("\n\n\n")
file.write(" Comments ")
file.write("\n")
file.write(" --------")
file.write("\n")
file.close()    
i = 1
comment_count = 0
print(f"{yellow} Commented Communities{reset} ")
print(" -------------------")
for comment in comments:
    if not comment.subreddit.display_name in comment_subreddits :
       subreddit = reddit.subreddit(comment.subreddit.display_name)
       description = subreddit.public_description
       print(f" {blue}[{green}*{blue}]{yellow} Index {white}:{green} {i}{reset}")
       print(f" {blue}[{green}*{blue}]{yellow} Date & Time {white}:{green} {datetime.datetime.fromtimestamp(comment.created_utc)}{reset}")
       print(f" {blue}[{green}*{blue}]{yellow} Community {white}:{green} {comment.subreddit.display_name}{reset}")
       print(f" {blue}[{green}*{blue}]{yellow} Description {white}:{green} {description}{reset}")
       print("")
       comment_subreddits.append(comment.subreddit.display_name)
       i = i + 1  
    comment_count = comment_count + 1
    total_subreddits.append(comment.subreddit.display_name)
    if comment_count == 1000 :
       comment_count = "1000+"
    file = open(f"{username}.osint","a",encoding="utf-8")
    file.write(f" [+] Index : {y}")
    file.write("\n")
    file.write(f" [+] Community : {comment.subreddit.display_name}")
    file.write("\n")
    file.write(f" [+] Url : {comment.submission.permalink}")
    file.write("\n")
    file.write(f" [+] Date & Time : {datetime.datetime.fromtimestamp(comment.created_utc)}")
    file.write("\n")
    file.write(f" [+] u/{comment.submission.author} : {comment.submission.title}")
    file.write("\n")
    file.write(f" [+] Body : {comment.submission.selftext}")
    file.write("\n")
    file.write(f" [+] Comment : {comment.body}")
    file.write("\n")
    file.write(f" [+] Score : {comment.submission.score}")
    file.write("\n" + "-" * 40 + "\n")
    file.close()
    y = y + 1   
all_communities = list(set(post_subreddits) | set(comment_subreddits))
total = len(all_communities)
print("")
print(f" {yellow}Information {reset}")
print(" ------------")
print("")
print(f" {blue}[{green}i{blue}]{yellow} Username {white}:{green} {username}{reset}")
print(f" {blue}[{green}i{blue}]{yellow} Post Karma {white}:{green} {post_karma}{reset}")
print(f" {blue}[{green}i{blue}]{yellow} Comment Karma {white}:{green} {comment_karma}{reset}")
print(f" {blue}[{green}i{blue}]{yellow} Created Date {white}:{green} {created_date}{reset}")
print(f" {blue}[{green}i{blue}]{yellow} Last seen Date {white}:{green} {lastseen_date}{reset}")
print(f" {blue}[{green}i{blue}]{yellow} Posted Communities {white}:{white} {str(post_subreddits)}{reset}")
print(f" {blue}[{green}i{blue}]{yellow} Commented Communities {white}:{white} {str(comment_subreddits)}{reset}")
print(f" {blue}[{green}i{blue}]{yellow} All Communities {white}:{white} {all_communities}{reset}")
print(f" {blue}[{green}i{blue}]{yellow} Total Communities {white}:{white} {total}{reset}")
print(f" {blue}[{green}i{blue}]{yellow} Total Posts {white}:{white} {post_count}{reset}")
print(f" {blue}[{green}i{blue}]{yellow} Total Comments {white}:{white} {comment_count}{reset}")
file = open(f"{username}.osint","a",encoding="utf-8")
file.write("\n\n\n")
file.write(" Information")
file.write("\n")
file.write(" -----------")
file.write("\n")
file.write(f" [-] Username : {username}")
file.write("\n")
file.write(f" [-] Post Karma : {post_karma}")
file.write("\n")
file.write(f" [-] Comment Karma : {comment_karma}")
file.write("\n")
file.write(f" [-] Created Date : {created_date}")
file.write("\n")
file.write(f" [-] Last Seen Date : {lastseen_date}")
file.write("\n")
file.write(f" [-] Posted Communities : {str(post_subreddits)}")
file.write("\n")
file.write(f" [-] Commented Communities : {str(comment_subreddits)}")
file.write("\n")
file.write(f" [-] All Communities : {all_communities}")
file.write("\n")
file.write(f" [-] Total Communities : {total}")
file.write("\n")
file.write(f" [-] Total Posts : {post_count}")
file.write("\n")
file.write(f" [-] Total Comments : {comment_count}")
file.write("\n\n")
file.close()
print("")
print(f"{yellow} Most Active Communities{reset} ")
print(" --------------------------")
count = Counter(total_subreddits)
most_active_communities = count.most_common(10)
file = open(f"{username}.osint","a",encoding="utf-8")
file.write(" Most Active Communities ")
file.write("\n")
file.write(" -----------------------")
file.write("\n")
for key,value in most_active_communities :
    print(f" {blue}[{green}-{blue}]{yellow} {key} {white}:{green} {value}{reset}")
    file.write(f" [-] {key} : {value}")
    file.write("\n")
file.close()
print(f"{reset}")
