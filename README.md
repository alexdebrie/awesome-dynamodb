<p align="center">
  <img src="https://user-images.githubusercontent.com/6509926/70553550-f033b980-1b40-11ea-9192-759b3b1053b3.png">
</p>

# Awesome DynamoDB 🚀

A handy list of resources for getting up to speed on modeling, operating, and using [Amazon DynamoDB](https://aws.amazon.com/dynamodb/).

Contributions welcome!

## Table of Contents

- [Rick Houlihan](#rick-houlihan)
- [Books](#books)
- [Videos](#videos)
- [Written resources](#written-resources)
- [Tools](#tools)
- [Uses](#uses)

## Rick Houlihan

[Rick Houlihan](https://twitter.com/houlihan_rick) gets his own section due to his mythical status among DynamoDB fans. His AWS re:Invent talks are always the most-watched sessions on YouTube. Rick is rarely seen outside his native habitat on the strip in Las Vegas or in the AWS War Room, but some astute developers have seen him in the wild, usually mumbling about how 'all data is relational'.

Rick's talks:

- [AWS re:Invent 2019: Advanced Design Patterns](https://t.co/fRtp2X3Vgg?amp=1)
- [AWS re:Invent 2018: Advanced Design Patterns](https://t.co/ivlcYMhkur?amp=1)
- [AWS re:Invent 2017: Advanced Design Patterns](https://t.co/b3OeDqBbBK?amp=1)
- [DynamoDB Office Hours | Online banking service model](https://www.twitch.tv/videos/689452191)

## Books

- [The DynamoDB Book](https://www.dynamodbbook.com/). Comprehensive guide to data modeling with DynamoDB. [Endorsed by Rick Houlihan](https://twitter.com/houlihan_rick/status/1247522640278859777) and heavily used within Amazon & AWS.

## Videos

- [AWS re:Invent 2018: DynamoDB Under the Hood](https://www.youtube.com/watch?v=yvBR71D0nAQ). Really great talk from a DynamoDB engineer that dives into the architecture behind DynamoDB.
- [AWS re:Invent 2019: Data Modeling with DynamoDB](https://www.youtube.com/watch?v=DIQVJqiSUkE). A more intermediate level talk that will explain some of the principles behind data modeling with DynamoDB.
- [DynamoDB Deep Dive (Course](https://linuxacademy.com/course/dynamo-db-deep-dive/). A full course from the folks at Linux Academy on how to use DynamoDB.
- [ServerlessConf 2019: Using (and Ignoring) DynamoDB Best Practices with Serverless](https://acloud.guru/series/serverlessconf-nyc-2019/view/dynamodb-best-practices). This talk focuses on using DynamoDB in Serverless applications.
- [DynamoDB Relationships](https://www.youtube.com/watch?v=lh7q5hCrCSU&list=PL6oNLEZTnXshgy4iHFULjYvcwbeMTotJp). A nice 30 minute video series from [Gary Jennings](https://twitter.com/G_Jennings09) that walks through examples of how to model different types of relationships in DynamoDB -- one-to-one, one-to-many, and many-to-many. Nice use of the NoSQL Workbench for DynamoDB as well.
- [Videos from The DynamoDB Book](https://www.youtube.com/playlist?list=PLNjt4IpUlQLieAf8YE4bjN7kgwntsfW_B). A playlist of three sample videos from The DynamoDB Book.

## Written resources

- [DynamoDB Best Practices Guide](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/best-practices.html). From the AWS documentation, a list of best practices and examples for modeling with DynamoDB.
- [DynamoDB Guide](https://www.dynamodbguide.com/). A basic walkthrough to DynamoDB concepts, API actions, and mechanics, with some data modeling examples.
- [From relational DB to single DynamoDB table: a step-by-step exploration](https://www.trek10.com/blog/dynamodb-single-table-relational-modeling/). Awesome post from [Forrest Brazeal](https://twitter.com/forrestbrazeal) with a step-by-step walkthrough of moving to a single-table design.
- [How to switch from RDBMS to DynamoDB in 20 easy steps...](https://www.jeremydaly.com/how-to-switch-from-rdbms-to-dynamodb-in-20-easy-steps/). By [Jeremy Daly](https://twitter.com/jeremy_daly), a funny and eternally useful list of steps for learning how to model with DynamoDB.
- [Comparing multi and single table approaches to designing a DynamoDB data model](https://winterwindsoftware.com/dynamodb-modelling-single-vs-multi-table/). [Paul Swail](https://twitter.com/paulswail) takes a look at the pros and cons of modeling with a single table in DynamoDB and provides recommendations on when to avoid it.
- [Lessons learned using Single-table design with DynamoDB and GraphQL in production](https://servicefull.cloud/blog/dynamodb-single-table-design-lessons/). A collection of great tips learned the hard way from [Rafal Wilinski](https://twitter.com/rafalwilinski). Rafal is the creator of Dynobase, listed in the [Tools](#tools) section below.
- [DynamoDB Document client cheatsheet](https://github.com/dabit3/dynamodb-documentclient-cheat-sheet). From the prolific [Nader Dabit](https://twitter.com/dabit3), this is a handy cheatsheet for using DynamoDB in JavaScript applications.

## Tools

- [Dynobase](https://dynobase.dev/). Handy tool that makes it easy to view and manipulate your tables, generate application code, and more.
- [NoSQL Workbench For Amazon DynamoDB](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/workbench.html). A tool similar MySQL workbench that lets you model data and interact with your tables without going to the AWS console.
- [DynamoDB Toolbox](https://github.com/jeremydaly/dynamodb-toolbox). An open source project from Jeremy Daly that provides a number of helpful utilities for working with single-table designs in JavaScript. Unofficial winner of the 2019 Best Logo in Open Source award.
- [Dynamoose](https://github.com/dynamoose/dynamoose/). An open source modeling tool for Node.js projects, inspired by Mongoose.
- [DynamoDB Read Stream](https://github.com/AlexHladin/dynamodb-read-stream). An open-source tool for reading data chunk by chunk. This tool is created for handling DynamoDB limitation for one response (1 MB).
- [DynamoDB Pricing Calculator](https://dynobase.dev/dynamodb-pricing-calculator/). Simple tool to calculate your DynamoDB costs
- [DynamoDB Table Designer](https://dynobase.dev/dynamodb-table-schema-design-tool/). Visual tool to help you create DynamoDB Table definitions without the knowledge of CreateTable syntax.
- [Dynoexpr](https://github.com/tuplo/dynoexpr) Typescript/Javascript expression builder library which immensely simplifies the DynamoDB.DocumentClient syntax.

## Uses

- [Priority Queuing](https://aws.amazon.com/blogs/database/implementing-priority-queueing-with-amazon-dynamodb/). This post describes how to convert any of your Amazon DynamoDB tables into a queue that can enqueue and dequeue, as you would do with any other large-scale queuing systems.
- [Near-Real-Time Event Processing](https://aws.amazon.com/blogs/database/how-to-perform-ordered-data-replication-between-applications-by-using-amazon-dynamodb-streams/). This post evaluates multiple patterns for processing DynamoDB streams by using several AWS services that are part of AWS serverless computing. It also dives into the details about the most reliable and scalable pattern to perform near-real-time processing of DynamoDB streams to notify other systems and users, archive transactions, and replicate data to other data stores while ensuring ordered processing.
- [Advanced Analytics & Visualizations](https://aws.amazon.com/blogs/database/how-to-perform-advanced-analytics-and-build-visualizations-of-your-amazon-dynamodb-data-by-using-amazon-athena/). This blog post shows you how to build a big data pipeline that transitions the data from your DynamoDB table to Amazon S3. This helps you perform advanced analytics by using Amazon Athena, a fully managed Presto query service, and also helps you build visualizations and ad hoc analyses by using Amazon QuickSight.
