library(crypto)

crypto_date <- crypto_history()

write.csv(crypto_date,
          file = "crypto_data.csv")

