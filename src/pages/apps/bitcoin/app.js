import React, { useState, useEffect } from 'react';
import { graphql } from "gatsby"

import Layout from "../../../components/layout"
import SEO from "../../../components/seo"

import './app.scss';

function App (){

  const [price, setPrice] = useState(0.0);

  // Similar to componentDidMount and componentDidUpdate:
  useEffect(() => {
    fetch('https://blockchain.info/ticker')
    .then(res => res.json())
    .then((data) => {
      // console.log(data['GBP']['last']);
      setPrice(parseFloat(data['GBP']['last']))
    })
    .catch(console.log);
  });

  return (
    <div className="apps-refresher-main">
      <header className="App-header">
        Current price for 1 bitcoin: <b>£{price}</b>
      </header>
    </div>
  );
}

class BitCoinApp extends React.Component {
  render() {
    const { data } = this.props
    const siteTitle = data.site.siteMetadata.title
    return (
      <Layout location={this.props.location} title={siteTitle}>
        <SEO title="Apps: Refresher" />
        <App />
      </Layout>
    )
  }
}

export default BitCoinApp;

export const pageQuery = graphql`
  query {
    site {
      siteMetadata {
        title
      }
    }
  }
`