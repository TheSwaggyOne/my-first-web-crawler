# my-first-web-crawler

Task description:

1. Find 1000 urls from common crawl archive that discuss or relevent to COVID-19's economic impact.

Problesm:

1. This is my first time wrote a web crawler, I spent most of time on how to acesss the data, research online on what tool I can use.
2. Still havn't find a way to access all the data using the links provided by common crawl archive. Since I don't have an AWS account, when I try to access the links that contain data, my access was denied. I find an alternative way to solve this problem inorder to demostrate my work. I used an example link I found which allow https request to access the data. However, the link contains only data from Jan 2022.

Failed Approach:

I tried to use regex function provided by python to search all the key words related to covid-19 in the entire html content from each link. If there is a match, the url is added into the output file. However, the false positive rate of this approach is very high, since the html/css files may contain code that is same to the key words, eg. id = covid, class = covid, but the content is not necessary related to economic impact due to covid-19. 

New Approach:

Matching algorithm: Using hot keys words which people use to search content that related to the economic impact of COVID-19. to match the urls' content.

In order to solve the previous issues, my thought is to focus searching on block with tag title and tag p (paragraph) in the html file, since these two block represent the main idea of the content in this most of time. The next question is how to only search within the title and p tag? After I did some research, I found this library called beautiful soup. This library provides powerful tool for crawling web which includes extract content of specific tag. 

Next step, simply just extract all the tags I needed, and use regular expression to find a match. Since each wrong link will deduct 1 pt, and my match algorithm is not very robust at the moment, I can image the false positive rate is going to be high. As a result, I decide to only add the link to the result, if and only if there are matches in both content of title and paragraph.

Future Improvement:

1. Figure out a way to access to the "real" common crawl archive database.
2. Due to the time limitation, I can't figure out how beautiful soup works, as a result maybe there are other powerful tool I can use to better complete the task, also without a better understanding of this library, I can't analyze the time complexity of this script. 
2. At the moment, I used the same matching algorithm for both title and paragraph, however, this method is not good enough, since title mostly illustrated the main idea of the content, and the paragraph dig deeper into that matter. As a result, It would be a better idea to have two separated algorithms for matching the title and the paragraph. Also, using information retrivel module such as BERT is even a better idea.
3. The script now only searchs the provided urls from the database, however, each url may contain other links that might have information we need. In order to fully utilize the resourses, It's better to dig deeper into the ref links in each url. To do this, initial thought is to use a queue to store all the ref links on current url, then search each ref link in the queue on by on. But doing this will cause a lot of time, some thoughts to improve that are add some filter algorithms that only add related links to the queue, and also maybe set a cap to limite the maximum call we are going to make. 
