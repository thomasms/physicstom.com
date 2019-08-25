import React from 'react';
import { graphql } from "gatsby"

import Layout from "../../components/layout"
import SEO from "../../components/seo"

import { instanceOf } from 'prop-types';
import { withCookies, Cookies } from 'react-cookie';
import { CookiesProvider } from 'react-cookie';

const COUNT_LIMIT = 200;

// can we use React hooks instead??
// probably but for now we do it the old 
// fashioned way
class Refresher extends React.Component {

    static propTypes = {
      cookies: instanceOf(Cookies).isRequired
    };

   constructor( props ) {
     super( props );

     const { cookies } = props;
     this.state = {
         count: parseInt(cookies.get('count')) || 0,
     };
   }

   componentDidMount(){
      const { cookies } = this.props;
      this.setState((prevState) => ({
          count: prevState.count + 1
      }), function () {cookies.set('count', this.state.count, { path: '/' })});
   }

   render(){
       var hidden = this.state.count > COUNT_LIMIT ? 
            <div>You are in!</div> : 
            <p>
              Number of hits: {this.state.count}
            </p>;

       return (
           
        <div className="App">
          <header className="App-header">
	    {hidden}
          </header>
        </div>
       );
   }
}

const RefresherWithCookies = withCookies(Refresher);

class RefresherApp extends React.Component {
    render() {
      const { data } = this.props
      const siteTitle = data.site.siteMetadata.title
      return (
        <Layout location={this.props.location} title={siteTitle}>
          <SEO title="Apps: Refresher" />
          <CookiesProvider><RefresherWithCookies/></CookiesProvider>
        </Layout>
      )
    }
  }

export default RefresherApp;

export const pageQuery = graphql`
  query {
    site {
      siteMetadata {
        title
      }
    }
  }
`