var jTrucks2 = {


		init: function() {
			/* Call on ready to initialize the needed functions */
			var self = this; // Cache this to reduce lookups
			self.tabs.init();
			self.ratings.init($('input[type=radio].rating-star'), $('form.rating_form'));
			self.rankings.init($('input.ranking_checkbox'), $('form.insightful_form'));
			self.carousels.init();
			self.login.init();
			self.comments.init();
			self.photos.init();
			self.videoPlayer.init();
			self.calendars.init();
			self.maps.init();
			self.mobile.init();
			self.staffmembers.init();
			self.cinemasource.init();
			self.apptap.init();
			self.browsers.init();
			self.socialShare.init();
		}



	}


	jTrucks.init();