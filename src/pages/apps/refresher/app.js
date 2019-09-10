import React from 'react';
import { graphql } from "gatsby"

import Layout from "../../../components/layout"
import SEO from "../../../components/seo"

import { instanceOf } from 'prop-types';
import { withCookies, Cookies } from 'react-cookie';
import { CookiesProvider } from 'react-cookie';

import './app.scss';

const COUNT_LIMIT = 200;

// can we use React hooks instead??
// for now we do it the old 
// fashioned way
class Refresher extends React.Component {

    static propTypes = {
      cookies: instanceOf(Cookies).isRequired
    };

   constructor( props ) {
     super( props );

     this.reset = this.reset.bind(this);

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

   reset(){
        const { cookies } = this.props;
        this.setState({
            count: 0
        }, function () {cookies.set('count', 0, { path: '/' })});
   }

   render(){
       var hidden = this.state.count > COUNT_LIMIT ? 
            <div>You are in!</div> : 
            <div>
                <p>
                Refresh me!
                </p>
                <p>
                Number of hits: {this.state.count}
                </p>
            </div>;

       return (
           
        <div className="apps-refresher-main">
          <header className="App-header">
            {hidden}
          </header><button class="button is-danger is-rounded" onClick={this.reset}>Reset</button>
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