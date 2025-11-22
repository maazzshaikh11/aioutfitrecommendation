import React from 'react';
import { Link } from 'react-router-dom';

const Home = () => {
  return (
    <div className="min-h-screen bg-gradient-to-br from-primary-50 via-white to-secondary-50">
      {/* Hero Section */}
      <section className="relative py-20 px-4">
        <div className="max-w-7xl mx-auto">
          <div className="grid md:grid-cols-2 gap-12 items-center">
            <div className="text-center md:text-left">
              <h1 className="text-4xl md:text-6xl font-black mb-6 bg-gradient-to-r from-primary-500 via-primary-600 to-secondary-400 bg-clip-text text-transparent leading-tight">
                Discover Your Unique Fashion Aesthetic
              </h1>
              <p className="text-xl text-gray-600 mb-8 leading-relaxed">
                Through AI-powered style analysis, find your perfect fashion identity and get personalized outfit recommendations that truly reflect who you are.
              </p>
              <div className="flex flex-col sm:flex-row gap-4 justify-center md:justify-start">
                <Link 
                  to="/quiz"
                  className="bg-gradient-to-r from-primary-500 to-primary-600 text-white px-8 py-4 rounded-2xl font-semibold text-lg hover:from-primary-600 hover:to-primary-700 transform hover:scale-105 transition-all duration-300 shadow-lg hover:shadow-xl"
                >
                  Start Style Quiz
                </Link>
                <Link 
                  to="/recommendations"
                  className="border-2 border-primary-500 text-primary-600 px-8 py-4 rounded-2xl font-semibold text-lg hover:bg-primary-500 hover:text-white transition-all duration-300"
                >
                  View Recommendations
                </Link>
              </div>
            </div>
            <div className="relative">
              <div className="relative z-10 bg-white rounded-3xl shadow-2xl overflow-hidden">
                <img 
                  src="https://images.pexels.com/photos/1926769/pexels-photo-1926769.jpeg?auto=compress&cs=tinysrgb&w=600" 
                  alt="Fashion AI" 
                  className="w-full h-96 object-cover"
                />
              </div>
              <div className="absolute -top-4 -right-4 w-full h-full bg-gradient-to-br from-primary-200 to-secondary-200 rounded-3xl z-0"></div>
            </div>
          </div>
        </div>
      </section>

      {/* Features Section */}
      <section className="py-20 px-4 bg-white">
        <div className="max-w-7xl mx-auto">
          <div className="text-center mb-16">
            <h2 className="text-4xl font-bold text-gray-900 mb-4">Why Choose StyleAI?</h2>
            <p className="text-xl text-gray-600">Discover your perfect style with AI-powered precision</p>
          </div>
          
          <div className="grid md:grid-cols-3 gap-8">
            <div className="text-center p-8 rounded-2xl bg-gradient-to-br from-primary-50 to-primary-100 border border-primary-200 hover:shadow-lg transition-all duration-300">
              <div className="text-5xl mb-6">🤖</div>
              <h3 className="text-2xl font-bold mb-4 text-gray-900">AI-Powered Analysis</h3>
              <p className="text-gray-600 leading-relaxed">
                Our intelligent quiz analyzes your preferences to determine your unique fashion aesthetic with precision.
              </p>
            </div>
            
            <div className="text-center p-8 rounded-2xl bg-gradient-to-br from-secondary-50 to-secondary-100 border border-secondary-200 hover:shadow-lg transition-all duration-300">
              <div className="text-5xl mb-6">✨</div>
              <h3 className="text-2xl font-bold mb-4 text-gray-900">Curated Recommendations</h3>
              <p className="text-gray-600 leading-relaxed">
                Get personalized outfit suggestions that match your style, budget, and preferences perfectly.
              </p>
            </div>

            <div className="text-center p-8 rounded-2xl bg-gradient-to-br from-accent-50 to-accent-100 border border-accent-200 hover:shadow-lg transition-all duration-300">
              <div className="text-5xl mb-6">🔥</div>
              <h3 className="text-2xl font-bold mb-4 text-gray-900">Trending Styles</h3>
              <p className="text-gray-600 leading-relaxed">
                Explore the latest fashion trends curated by our AI engine to keep your wardrobe fresh.
              </p>
            </div>
          </div>
        </div>
      </section>

      {/* Replacing OLD Community Section with Trending Fashion Section */}
      <section className="py-20 px-4 bg-gradient-to-br from-white to-primary-50">
        <div className="max-w-7xl mx-auto">
          <div className="text-center mb-16">
            <h2 className="text-4xl font-bold text-gray-900 mb-4">Trending Fashion Picks</h2>
            <p className="text-xl text-gray-600">Stay ahead with AI-selected style inspirations</p>
          </div>

          <div className="grid md:grid-cols-3 gap-10">
            <div className="bg-white shadow-lg rounded-2xl overflow-hidden hover:shadow-xl transition-all duration-300 border border-gray-100">
              <img src="https://images.pexels.com/photos/2983464/pexels-photo-2983464.jpeg?auto=compress&cs=tinysrgb&w=600" className="h-64 w-full object-cover" />
              <div className="p-6 text-center">
                <h3 className="text-xl font-bold mb-2 text-gray-900">Soft Aesthetic</h3>
                <p className="text-gray-600 text-sm">Pastel tones • Light fabrics • Calm & cozy vibes</p>
              </div>
            </div>

            <div className="bg-white shadow-lg rounded-2xl overflow-hidden hover:shadow-xl transition-all duration-300 border border-gray-100">
              <img src="https://images.pexels.com/photos/7679727/pexels-photo-7679727.jpeg?auto=compress&cs=tinysrgb&w=600" className="h-64 w-full object-cover" />
              <div className="p-6 text-center">
                <h3 className="text-xl font-bold mb-2 text-gray-900">Streetwear Edge</h3>
                <p className="text-gray-600 text-sm">Oversized fits • Monochrome • Bold accessories</p>
              </div>
            </div>

            <div className="bg-white shadow-lg rounded-2xl overflow-hidden hover:shadow-xl transition-all duration-300 border border-gray-100">
              <img src="https://images.pexels.com/photos/1036623/pexels-photo-1036623.jpeg?auto=compress&cs=tinysrgb&w=600" className="h-64 w-full object-cover" />
              <div className="p-6 text-center">
                <h3 className="text-xl font-bold mb-2 text-gray-900">Vintage Revival</h3>
                <p className="text-gray-600 text-sm">Retro jackets • Warm palettes • 90s energy</p>
              </div>
            </div>
          </div>
        </div>
      </section>

      {/* CTA */}
      <section className="py-20 px-4 bg-gradient-to-r from-primary-500 to-secondary-500 text-white">
        <div className="max-w-4xl mx-auto text-center">
          <h2 className="text-4xl font-bold mb-6">Ready to Transform Your Style?</h2>
          <p className="text-xl mb-8 opacity-90">
            Take our AI-powered quiz and discover your perfect fashion aesthetic in minutes
          </p>
          <Link 
            to="/quiz"
            className="bg-white text-primary-600 px-10 py-4 rounded-2xl font-bold text-lg hover:bg-gray-100 transition-colors duration-300 inline-block shadow-lg"
          >
            Start Your Style Journey
          </Link>
        </div>
      </section>
    </div>
  );
};

export default Home;
