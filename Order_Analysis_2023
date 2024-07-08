#Analyzing 2023 Orders for OnlyNY & getting Deferred Revenue stats

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
shopify_orders3 <- data.frame(read_csv("/cloud/project/Order_Data/orders_export_3.csv"))
shopify_orders4 <- data.frame(read_csv("/cloud/project/Order_Data/orders_export_4.csv"))

#Viewing file and basic data manipulations

str(shopify_orders1)
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


combined_2023 <- rbind(shopify_orders1,shopify_orders2,shopify_orders3,shopify_orders4)


#Stats on combined sheets


combined_2023_statistics  <- combined_2023 %>% select(1, 9, 10, 11, 12, 14, 50) %>% summarise(OrderCount=n_distinct(Name),
                                                                                                  SubtotalSum=sum(Subtotal,na.rm=T),
                                                                                                  ShippingSum=sum(Shipping,na.rm=T),
                                                                                                  TaxSum=sum(Taxes,na.rm=T),
                                                                                                  DiscountSum=sum(Discount.Amount,na.rm=T),
                                                                                                  RefundSum=sum(Refunded.Amount,na.rm=T),
                                                                                                  TotalSum=sum(Total,na.rm=T))

view(combined_2023_statistics)

write.csv(combined_2023, "/cloud/project/Order_Data/shopify_orders_combined_2023.csv", row.names=FALSE)

#Export of the file if needed
##write.csv(shopify_orders_combined_2023, "/cloud/project/Order_Data/shopify_orders_combined_2023.csv", row.names=FALSE)


#Months on combined sheets, omg so beautiful. Also added a sum there at the end. 

combined_2023_dates <- (combined_2023) %>% 
  group_by("Year"=year(Created.at) ,"Month"=month(Created.at,label=T)) %>% 
  summarise("Number of Orders"=n_distinct(Name),
            SubtotalSum=sum(Subtotal,na.rm=T),
            ShippingSum=sum(Shipping,na.rm=T),
            TaxSum=sum(Taxes,na.rm=T),
            DiscountSum=sum(Discount.Amount,na.rm=T),
            RefundSum=sum(Refunded.Amount,na.rm=T),
            TotalSum=sum(Total,na.rm=T))  %>%
  adorn_totals("row")

view(combined_2023_dates)

write.csv(combined_2023_dates, "/cloud/project/Order_Data/combined_2023_dates.csv", row.names=FALSE)


#Combined Sheets grouped by order to avoid the N/A's and to get relevant columns to determine deferred revenue etc

#Im having issues with the "Fulfilled at" and the "Paid at" columns, I think that this is because of the N/As that they have and im not sure gow to solve this


combined_2023_groupedbyfulfillment <- combined_2023 %>% 
  drop_na(Subtotal) %>% 
  group_by("Month"=my(as.Date(Created.at),label=T),Fulfillment.Status,Financial.Status,"Month Fulfilled"=month(as.Date(Fulfilled.at),label=T),Payment.Method,Source,Location) %>%
  select(1,3, 4, 5, 6, 6, 59, 54, 9, 10, 11, 12, 14, 16, 20, 47, 48, 50) %>% 
  summarise("Number of Orders"=n_distinct(Name),
            SubtotalSum=sum(Subtotal,na.rm=T),
            ShippingSum=sum(Shipping,na.rm=T),
            TaxSum=sum(Taxes,na.rm=T),
            DiscountSum=sum(Discount.Amount,na.rm=T),
            RefundSum=sum(Refunded.Amount,na.rm=T),
            TotalSum=sum(Total,na.rm=T))  %>%
  adorn_totals("row")


write.csv(combined_2023_groupedbyfulfillment, "/cloud/project/Order_Data/combined_2023_groupedbyfulfillment.csv", row.names=FALSE)


view(combined_2023_groupedbyfulfillment)


###group_by("Year"=year(Created.at) ,"Month"=month(Created.at,label=T), "Fufillment_Type"=Fulfillment.Status) %>%  summarise("Order_Count"=n_distinct(Name))
