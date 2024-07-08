#Analyzing 2024 Orders for OnlyNY & getting Deferred Revenue stats

#What packages will I need?
install.packages("tidyverse")
install.packages("lubridate")
install.packages("janitor")
install.packages("dplyr")


#loading packages

library(tidyverse)
library(lubridate) 
library(dplyr)
library(janitor)


#importing Files, its easier to work with data frames. importing without specifying its a data frame creates a list :(, I think. For some reason this works. 

shopify_orders1 <- data.frame(read_csv("/cloud/project/Order_Data/orders_export_1.csv"))
shopify_orders2 <- data.frame(read_csv("/cloud/project/Order_Data/orders_export_2.csv"))

#Viewing file and basic data manipulations

str(shopify_orders2)
glimpse(shopify_orders1)
view(shopify_orders1)


###There seem to be some data issues but doesn't seem to affect too many of them
#problems(shopify_orders1)
#problems(shopify_orders2)
#problems(shopify_orders3)
#problems(shopify_orders4)


#Simple statistics summarized for sheet and viewed


shopify_orders1_statistics  <- shopify_orders1 %>% select(1, 9, 10, 11, 12, 14, 50) %>% summarise(OrderCount=n_distinct(Name),
                                                                                                  SubtotalSum=sum(Subtotal,na.rm=T),
                                                                                                  ShippingSum=sum(Shipping,na.rm=T),
                                                                                                  TaxSum=sum(Taxes,na.rm=T),
                                                                                                  DiscountSum=sum(Discount.Amount,na.rm=T),
                                                                                                  RefundSum=sum(Refunded.Amount,na.rm=T),
                                                                                                  TotalSum=sum(Total,na.rm=T))

                                                                                                     
view(shopify_orders1_statistics)


#Want to see which months are represented and how many orders in each month, view() function

shopify_orders1_dates <- (shopify_orders1) %>% group_by("Year"=year(Created.at) ,"Month"=month(Created.at,label=T)) %>% summarise("Number of Orders"=n_distinct(Name))


view(shopify_orders1_dates)





#How can we combine sheets


combined_2024_Q1 <- rbind(shopify_orders1,shopify_orders2)


#Stats on combined sheets


combined_2024_Q1_statistics  <- combined_2024_Q1 %>% select(1, 9, 10, 11, 12, 14, 50) %>% summarise(OrderCount=n_distinct(Name),
                                                                                                  SubtotalSum=sum(Subtotal,na.rm=T),
                                                                                                  ShippingSum=sum(Shipping,na.rm=T),
                                                                                                  TaxSum=sum(Taxes,na.rm=T),
                                                                                                  DiscountSum=sum(Discount.Amount,na.rm=T),
                                                                                                  RefundSum=sum(Refunded.Amount,na.rm=T),
                                                                                                  TotalSum=sum(Total,na.rm=T))

view(combined_2024_Q1_statistics)

write.csv(combined_2024_Q1, "/cloud/project/Order_Data/shopify_orders_combined_2024_Q1.csv", row.names=FALSE)

#Export of the file if needed
##write.csv(shopify_orders_combined_2024_Q1, "/cloud/project/Order_Data/shopify_orders_combined_2024_Q1.csv", row.names=FALSE)


#Months on combined sheets, omg so beautiful. Also added a sum there at the end. 

combined_2024_Q1_dates <- (combined_2024_Q1) %>% 
  group_by("Year"=year(Created.at) ,"Month"=month(Created.at,label=T)) %>% 
  summarise("Number of Orders"=n_distinct(Name),
            SubtotalSum=sum(Subtotal,na.rm=T),
            ShippingSum=sum(Shipping,na.rm=T),
            TaxSum=sum(Taxes,na.rm=T),
            DiscountSum=sum(Discount.Amount,na.rm=T),
            RefundSum=sum(Refunded.Amount,na.rm=T),
            TotalSum=sum(Total,na.rm=T))  %>%
  adorn_totals("row")

view(combined_2024_Q1_dates)

write.csv(combined_2024_Q1_dates, "/cloud/project/Order_Data/combined_2024_Q1_dates.csv", row.names=FALSE)
