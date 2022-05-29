import React, { Component } from "react"
import { graphql } from "gatsby"

import Layout from "../../../components/layout"
import Seo from "../../../components/seo"

import Table from "./Table.js"

class App extends Component {
  render() {
    return (
      <div>
        <div className="apps-periodictable-header">
          <p>Periodic Table</p>
        </div>

        <div className="apps-periodictable-main">
          <Table />
        </div>
      </div>
    )
  }
}

class PeriodicTableApp extends React.Component {
  render() {
    const { data } = this.props
    const siteTitle = data.site.siteMetadata.title
    return (
      <Layout location={this.props.location} title={siteTitle}>
        <Seo title="Apps: PeriodicTable" />
        <App />
      </Layout>
    )
  }
}

export default PeriodicTableApp

export const pageQuery = graphql`
  query {
    site {
      siteMetadata {
        title
      }
    }
  }
`
