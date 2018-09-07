class UrlController < ApplicationController
    def index
    end
  
    def about
    end
  
    def show
      url = params[:id]
      @url = ShortUrl.where(["url = ?", url]).first
      if @url.nil?
        return redirect_to action: 'index', status: 307
      else
        return redirect_to @url
        end
end
