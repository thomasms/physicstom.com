import React, { useState, useEffect } from "react"
import { graphql } from "gatsby"
import { Line } from "react-chartjs-2"

import Layout from "../../../components/layout"
import SEO from "../../../components/seo"

import "./app.scss"

const plot_options = {
  // animation: {
  //   y: {
  //     easing: "easeInOutElastic",
  //     from: 0,
  //   },
  // },
  legend: {
    display: false,
  },
  tooltips: {
    enabled: true,
  },
  scales: {
    xAxes: [
      {
        display: false,
        gridLines: {
          display: false,
        },
      },
    ],
    yAxes: [
      {
        gridLines: {
          display: false,
        },
      },
    ],
  },
}

const HISTORICAL_PRICE_URL = `https://api.coindesk.com/v1/bpi/historical/close.json`
const CURRENT_PRICE_URL = `https://api.coindesk.com/v1/bpi/currentprice.json`

function App() {
  const [price, setPrice] = useState(0.0)
  const [historicalPrices, setHistoricalPrices] = useState([])

  useEffect(() => {
    fetch(CURRENT_PRICE_URL)
      .then(res => res.json())
      .then(data => {
        const price = parseFloat(data["bpi"]["USD"]["rate"].replace(",", ""))
        setPrice(price)
        return price
      })
      .then(price =>
        fetch(HISTORICAL_PRICE_URL)
          .then(res => res.json())
          .then(data => {
            // console.log(data["bpi"])
            var prices = []
            for (const [key, value] of Object.entries(data["bpi"])) {
              prices.push({ date: key, value: parseFloat(value) })
            }
            setHistoricalPrices([...prices, { date: "now", value: price }])
          })
      )
      .catch(console.log)
  }, [])

  const line_data = {
    // add an extra label with null to make the final marker visible
    labels: [...historicalPrices.map(item => item.date), ""],
    datasets: [
      {
        label: "$",
        data: historicalPrices.map(item => item.value),
        fill: false,
        borderColor: "rgba(255, 87, 51, 0.8)",
        pointBackgroundColor: [
          ...historicalPrices
            .slice(0, historicalPrices.length - 1)
            .map(item => "white"),
          "red",
        ],
        pointRadius: 4,
        pointHoverRadius: 10,
      },
    ],
  }

  return (
    <div className="apps-bitcoin-main">
      <header className="App-header">
        Current price for 1 bitcoin: <b>$ {price.toLocaleString("en")}</b>
      </header>
      <div className={"bitcoin-chart"}>
        <h4>Recent trend</h4>
        <Line data={line_data} options={plot_options} />
      </div>
      <footer className="bitcoin-note">
        <div class="content has-text-centered">
          <p>
            Powered by{" "}
            <a href="https://www.coindesk.com/price/bitcoin">CoinDesk</a>{" "}
          </p>
        </div>
      </footer>
    </div>
  )
}

const BitCoinApp = ({ data, location }) => {
  const siteTitle = data.site.siteMetadata.title
  return (
    <Layout location={location} title={siteTitle}>
      <SEO title="Apps: Bitcoin tracker" />
      <App />
    </Layout>
  )
}

export default BitCoinApp

export const pageQuery = graphql`
  query {
    site {
      siteMetadata {
        title
      }
    }
  }
`
