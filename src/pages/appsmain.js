import React from "react"
import { Link, graphql } from "gatsby"

import Layout from "../components/layout"
import Seo from "../components/seo"

const Apps = ({ data, location }) => {
  const siteTitle = data.site.siteMetadata.title

  const makeApp = (link, name, desc) => {
    return (
      <div
        className="card"
        style={{ marginTop: 10, marginBottom: 10, borderRadius: 20 }}
      >
        <div className="card-content">
          <Link
            style={{
              boxShadow: `none`,
              textDecoration: `none`,
              color: `inherit`,
            }}
            to={link}
          >
            <p className="title">{name}</p>
            <p className="subtitle">{desc}</p>
          </Link>
        </div>
      </div>
    )
  }

  const apps = [
    makeApp(
      `/apps/refresher/app`,
      `Refresher`,
      `A simple app using cookies to log number of attempts and refreshes to a site`
    ),
    makeApp(
      `/apps/periodictable/app`,
      "Periodic Table",
      "A complete and interactive periodic table"
    ),
    makeApp(
      `/apps/bitcoin/app`,
      "Bitcoin tracker",
      "Provides latest price of bitcoin"
    ),
  ]

  return (
    <div>
      <Layout location={location} title={siteTitle}>
        <Seo title="React Single Page Apps" />
        <div className="apps-title">Mini-apps</div>
        {apps.map((item, i) => (
          <div key={i}>{item}</div>
        ))}
      </Layout>
    </div>
  )
}

export default Apps

export const pageQuery = graphql`
  query {
    site {
      siteMetadata {
        title
      }
    }
  }
`
