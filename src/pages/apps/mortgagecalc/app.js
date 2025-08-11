import React, { useState, useEffect } from "react"
import { graphql } from "gatsby"

import Layout from "../../../components/layout"
import Seo from "../../../components/seo"

import "./app.scss"

function getInterestPerMonth(interestRatePerYear) {
  let interestRatePerMonth = Math.pow(1.0 + interestRatePerYear, 1.0 / 12.0)
  // We do not consider anything more than 1e-5 for rate
  interestRatePerMonth = parseFloat(interestRatePerMonth.toFixed(5))
  return interestRatePerMonth - 1
}

function getMonthlyPayment(principle, interestRatePerYear, periodInYears) {
  /**
   * Takes the interest rate per year and the number of years and calculates the monthly payment.
   * The interest rate is converted to a monthly rate.
   */
  const periodInMonths = periodInYears * 12
  const interestRatePerMonth = getInterestPerMonth(interestRatePerYear) + 1.0
  let d = 0
  for (let i = 0; i < periodInMonths; i++) {
    d += Math.pow(interestRatePerMonth, i)
  }
  // Anything less than a penny is dropped
  const monthlyPayment =
    ((principle * Math.pow(interestRatePerMonth, periodInMonths)) / d) * 100
  return Math.floor(monthlyPayment) / 100
}

function App() {
  const [interestRate, setInterestRate] = useState(3.2)
  const [principle, setPrinciple] = useState(300000)
  const [periodInYears, setPeriodInYears] = useState(25)

  const [monthlyPayment, setMonthlyPayment] = useState(0)

  // Convert interest rate to decimal for calculation
  const decimalInterestRate = interestRate / 100

  useEffect(() => {
    setMonthlyPayment(
      getMonthlyPayment(principle, decimalInterestRate, periodInYears)
    )
  }, [principle, decimalInterestRate, periodInYears])

  return (
    <div className="apps-mortgage-main">
      <header className="App-header">
        Based on the below inputs, the monthly payment is: {""}
        <span className="payment-display">
          {monthlyPayment.toLocaleString("en", { useGrouping: true })}
        </span>
      </header>
      <div className="input-container">
        <div className="input-group">
          <label htmlFor="input-principle">Principle:</label>
          <input
            id="input-principle"
            type="number"
            value={principle}
            step="100"
            onChange={(e) => {
              setPrinciple(e.target.value)
              setMonthlyPayment(
                getMonthlyPayment(
                  e.target.value,
                  decimalInterestRate,
                  periodInYears
                )
              )
            }}
          />
        </div>
        <div className="input-group">
          <br />
          <label htmlFor="input-interest">Interest rate (%):</label>
          <input
            id="input-interest"
            type="number"
            value={interestRate}
            onChange={(e) => {
              const newRate = e.target.value
              setInterestRate(newRate)
              setMonthlyPayment(
                getMonthlyPayment(principle, newRate / 100, periodInYears)
              )
            }}
          />
          <br />
        </div>
        <div className="input-group">
          <label htmlFor="input-period">Period (years):</label>
          <input
            id="input-period"
            type="number"
            value={periodInYears}
            onChange={(e) => {
              setPeriodInYears(e.target.value)
              setMonthlyPayment(
                getMonthlyPayment(
                  principle,
                  decimalInterestRate,
                  e.target.value
                )
              )
            }}
          />
        </div>
      </div>
    </div>
  )
}

const MortgageCalcApp = ({ data, location }) => {
  const siteTitle = data.site.siteMetadata.title
  return (
    <Layout location={location} title={siteTitle}>
      <Seo title="Apps: Mortgage calculator" />
      <App />
    </Layout>
  )
}

export default MortgageCalcApp

export const pageQuery = graphql`
  query {
    site {
      siteMetadata {
        title
      }
    }
  }
`
