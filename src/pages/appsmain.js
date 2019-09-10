import React from "react"
import { Link, graphql } from "gatsby"

import Layout from "../components/layout"
import SEO from "../components/seo"

class Apps extends React.Component {
  render() {
    const { data } = this.props
    const siteTitle = data.site.siteMetadata.title

    return (
      <div>

        <Layout location={this.props.location} title={siteTitle}>
          <SEO title="React Single Page Apps" />
          <div className="apps-title">
            Apps
          </div>

          <div className="card">
            <div className="card-content">
              <Link
              style={{
                  boxShadow: `none`,
                  textDecoration: `none`,
                  color: `inherit`,
              }}
              to={`/apps/refresher/app`}
              >
                <p className="title">
                  Refresher
                </p>
                <p className="subtitle">
                  A simple app using cookies to log number of attempts and refreshes to a site
                </p>
              </Link>
            </div>
          </div>
            
          <div className="card">
            <div className="card-content">
              <Link
              style={{
                  boxShadow: `none`,
                  textDecoration: `none`,
                  color: `inherit`,
              }}
              to={`/apps/periodictable/app`}
              >
                <p className="title">
                  Periodic Table
                </p>
                <p className="subtitle">
                  A complete and interactive periodic table
                </p>
              </Link>
            </div>
          </div>
        </Layout>
      </div>
    )
  }
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
