library(shiny)
# install.packages("shiny")
# Define UI for application that plots random distributions 
shinyUI(pageWithSidebar(
  
  # Application title
  headerPanel("URL-IP"),
  
  # Sidebar with a slider input for number of observations
  sidebarPanel(
   # sliderInput("obs", 
   #             "Number of observations:", 
   #             min = 0, 
   #             max = 1000, 
   #             value = 500)
  ),
  
  # Show a plot of the generated distribution
  mainPanel(
    tabsetPanel(
      tabPanel("Kmean", plotOutput("kmeanplot")), 
      tabPanel("DBSCAN", plotOutput("dbplot")), 
      tabPanel("Frenquency", plotOutput("table")),
      tabPanel("Preference", plotOutput("preference"))
    )
  )
))


