
library(poweRlaw)
HUMOR_INOUTDEGREEDIST$Ln_Out_Degree = log(HUMOR_INOUTDEGREEDIST$`Out-Degree` + 1)
data = subset(HUMOR_INOUTDEGREEDIST, HUMOR_INOUTDEGREEDIST$Ln_Out_Degree > 0)
m_bl = conpl$new(data$Ln_Out_Degree)
est = estimate_xmin(m_bl)
 m_bl$setXmin(est)
plot(m_bl, ylab = "Number of nodes", xlab = "Out Degree", main = "Humor")
lines(m_bl, col=2, lwd=2)


HUMOR_INOUTDEGREEDIST$Ln_In_Degree = log(HUMOR_INOUTDEGREEDIST$`In-Degree` + 1)
data = subset(HUMOR_INOUTDEGREEDIST, HUMOR_INOUTDEGREEDIST$Ln_In_Degree > 0)
m_bl = conpl$new(data$Ln_In_Degree)
est = estimate_xmin(m_bl)
m_bl$setXmin(est)

plot(m_bl, ylab = "Number of nodes", xlab = "In Degree", main = "Humor")
lines(m_bl, col=2, lwd=2)

DEPRESSION_INOUTDEGREEDIST$Ln_In_Degree = log(DEPRESSION_INOUTDEGREEDIST$`In-Degree` + 1)
data = subset(DEPRESSION_INOUTDEGREEDIST, DEPRESSION_INOUTDEGREEDIST$Ln_In_Degree > 0)
m_bl = conpl$new(data$Ln_In_Degree)
est = estimate_xmin(m_bl)
m_bl$setXmin(est)

plot(m_bl, ylab = "Number of nodes", xlab = "In Degree", main = "Depression")
lines(m_bl, col=2, lwd=2)

DEPRESSION_INOUTDEGREEDIST$Ln_Out_Degree = log(DEPRESSION_INOUTDEGREEDIST$`Out-Degree` + 1)
data = subset(DEPRESSION_INOUTDEGREEDIST, DEPRESSION_INOUTDEGREEDIST$Ln_Out_Degree > 0)
m_bl = conpl$new(data$Ln_Out_Degree)
est = estimate_xmin(m_bl)
m_bl$setXmin(est)

plot(m_bl, ylab = "Number of nodes", xlab = "Out Degree", main = "Depression")
lines(m_bl, col=2, lwd=2)


INSIGHTFUL_INOUTDEGREEDIST$Ln_Out_Degree = log(INSIGHTFUL_INOUTDEGREEDIST$`Out-Degree` + 1)
data = subset(INSIGHTFUL_INOUTDEGREEDIST, INSIGHTFUL_INOUTDEGREEDIST$Ln_Out_Degree > 0)
m_bl = conpl$new(data$Ln_Out_Degree)
est = estimate_xmin(m_bl)
m_bl$setXmin(est)

plot(m_bl, ylab = "Number of nodes", xlab = "Out Degree", main = "Insightful Questions")
lines(m_bl, col=2, lwd=2)


INSIGHTFUL_INOUTDEGREEDIST$Ln_In_Degree = log(INSIGHTFUL_INOUTDEGREEDIST$`In-Degree` + 1)
data = subset(INSIGHTFUL_INOUTDEGREEDIST, INSIGHTFUL_INOUTDEGREEDIST$Ln_In_Degree > 0)
m_bl = conpl$new(data$Ln_In_Degree)
est = estimate_xmin(m_bl)
m_bl$setXmin(est)

plot(m_bl, ylab = "Number of nodes", xlab = "In Degree", main = "Insightful Questions")
lines(m_bl, col=2, lwd=2)



SRS_INOUTDEGREEDIST$Ln_Out_Degree = log(SRS_INOUTDEGREEDIST$`Out-Degree` + 1)
data = subset(SRS_INOUTDEGREEDIST, SRS_INOUTDEGREEDIST$Ln_Out_Degree > 0)
m_bl = conpl$new(data$Ln_Out_Degree)
est = estimate_xmin(m_bl)
m_bl$setXmin(est)

plot(m_bl, ylab = "Number of nodes", xlab = "Out Degree", main = "SRS")
lines(m_bl, col=2, lwd=2)

SRS_INOUTDEGREEDIST$Ln_In_Degree = log(SRS_INOUTDEGREEDIST$`In-Degree` + 1)
data = subset(SRS_INOUTDEGREEDIST, SRS_INOUTDEGREEDIST$Ln_In_Degree > 0)
m_bl = conpl$new(data$Ln_In_Degree)
est = estimate_xmin(m_bl)
m_bl$setXmin(est)

plot(m_bl, ylab = "Number of nodes", xlab = "In Degree", main = "SRS")
lines(m_bl, col=2, lwd=2)


PROGRAMMERHUMOR_INOUTDEGREEDIST$Ln_In_Degree = log(PROGRAMMERHUMOR_INOUTDEGREEDIST$`In-Degree` + 1)
data = subset(PROGRAMMERHUMOR_INOUTDEGREEDIST, PROGRAMMERHUMOR_INOUTDEGREEDIST$Ln_In_Degree > 0)
m_bl = conpl$new(data$Ln_In_Degree)
est = estimate_xmin(m_bl)
m_bl$setXmin(est)

plot(m_bl, ylab = "Number of nodes", xlab = "In Degree", main = "Programmer Humor")
lines(m_bl, col=2, lwd=2)


PROGRAMMERHUMOR_INOUTDEGREEDIST$Ln_Out_Degree = log(PROGRAMMERHUMOR_INOUTDEGREEDIST$`Out-Degree` + 1)
data = subset(PROGRAMMERHUMOR_INOUTDEGREEDIST, PROGRAMMERHUMOR_INOUTDEGREEDIST$Ln_Out_Degree > 0)
m_bl = conpl$new(data$Ln_Out_Degree)
est = estimate_xmin(m_bl)
m_bl$setXmin(est)

plot(m_bl, ylab = "Number of nodes", xlab = "Out Degree", main = "Programmer Humor")
lines(m_bl, col=2, lwd=2)


SUICIDEWATCH_INOUTDEGREEDIST$Ln_Out_Degree = log(SUICIDEWATCH_INOUTDEGREEDIST$`Out-Degree` + 1)
data = subset(SUICIDEWATCH_INOUTDEGREEDIST, SUICIDEWATCH_INOUTDEGREEDIST$Ln_Out_Degree > 0)
m_bl = conpl$new(data$Ln_Out_Degree)
est = estimate_xmin(m_bl)
m_bl$setXmin(est)

plot(m_bl, ylab = "Number of nodes", xlab = "Out Degree", main = "Suicide Watch")
lines(m_bl, col=2, lwd=2)

SUICIDEWATCH_INOUTDEGREEDIST$Ln_In_Degree = log(SUICIDEWATCH_INOUTDEGREEDIST$`In-Degree` + 1)
data = subset(SUICIDEWATCH_INOUTDEGREEDIST, SUICIDEWATCH_INOUTDEGREEDIST$Ln_In_Degree > 0)
m_bl = conpl$new(data$Ln_In_Degree)
est = estimate_xmin(m_bl)
m_bl$setXmin(est)

plot(m_bl, ylab = "Number of nodes", xlab = "In Degree", main = "Suicide Watch")
lines(m_bl, col=2, lwd=2)

PTSD_INOUTDEGREEDIST$Ln_In_Degree = log(PTSD_INOUTDEGREEDIST$`In-Degree` + 1)
data = subset(PTSD_INOUTDEGREEDIST, PTSD_INOUTDEGREEDIST$Ln_In_Degree > 0)
m_bl = conpl$new(data$Ln_In_Degree)
est = estimate_xmin(m_bl)
m_bl$setXmin(est)

plot(m_bl, ylab = "Number of nodes", xlab = "In Degree", main = "PTSD")
lines(m_bl, col=2, lwd=2)

PTSD_INOUTDEGREEDIST$Ln_Out_Degree = log(PTSD_INOUTDEGREEDIST$`Out-Degree` + 1)
data = subset(PTSD_INOUTDEGREEDIST, PTSD_INOUTDEGREEDIST$Ln_Out_Degree > 0)
m_bl = conpl$new(data$Ln_Out_Degree)
est = estimate_xmin(m_bl)
m_bl$setXmin(est)

plot(m_bl, ylab = "Number of nodes", xlab = "Out Degree", main = "PTSD")
lines(m_bl, col=2, lwd=2)


CHANGEMYVIEW_INOUTDEGREEDIST$Ln_Out_Degree = log(CHANGEMYVIEW_INOUTDEGREEDIST$`Out-Degree` + 1)
data = subset(CHANGEMYVIEW_INOUTDEGREEDIST, CHANGEMYVIEW_INOUTDEGREEDIST$Ln_Out_Degree > 0)
m_bl = conpl$new(data$Ln_Out_Degree)
est = estimate_xmin(m_bl)
m_bl$setXmin(est)

plot(m_bl, ylab = "Number of nodes", xlab = "Out Degree", main = "Change My View")
lines(m_bl, col=2, lwd=2)

CHANGEMYVIEW_INOUTDEGREEDIST$Ln_In_Degree = log(CHANGEMYVIEW_INOUTDEGREEDIST$`In-Degree` + 1)
data = subset(CHANGEMYVIEW_INOUTDEGREEDIST, CHANGEMYVIEW_INOUTDEGREEDIST$Ln_In_Degree > 0)
m_bl = conpl$new(data$Ln_In_Degree)
est = estimate_xmin(m_bl)
m_bl$setXmin(est)

plot(m_bl, ylab = "Number of nodes", xlab = "In Degree", main = "Change My View")
lines(m_bl, col=2, lwd=2)


funny_deg_out$Ln_In_Degree = log(funny_deg_out$In + 1)
data = subset(funny_deg_out, funny_deg_out$Ln_In_Degree > 0)
m_bl = conpl$new(data$Ln_In_Degree)
est = estimate_xmin(m_bl)
m_bl$setXmin(est)

plot(m_bl, ylab = "Number of nodes", xlab = "In Degree", main = "Funny")
lines(m_bl, col=2, lwd=2)


funny_deg_out$Ln_Out_Degree = log(funny_deg_out$Out + 1)
data = subset(funny_deg_out, funny_deg_out$Ln_Out_Degree > 0)
m_bl = conpl$new(data$Ln_Out_Degree)
est = estimate_xmin(m_bl)
m_bl$setXmin(est)

plot(m_bl, ylab = "Number of nodes", xlab = "Out Degree", main = "Funny")
lines(m_bl, col=2, lwd=2)


